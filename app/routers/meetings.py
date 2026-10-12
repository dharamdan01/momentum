from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from datetime import datetime
import os
import shutil

from ..database import get_db
from ..models import Meeting, Task, Member
from ..schemas import MeetingCreate, MeetingOut
from ..services.mom_generator import transcribe_audio, generate_mom, extract_tasks

router = APIRouter(prefix="/api/meetings", tags=["meetings"])

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "uploads")


@router.get("/", response_model=list[MeetingOut])
def list_meetings(db: Session = Depends(get_db)):
    return db.query(Meeting).order_by(Meeting.date.desc()).all()


@router.get("/{meeting_id}", response_model=MeetingOut)
def get_meeting(meeting_id: int, db: Session = Depends(get_db)):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return meeting


@router.post("/", response_model=MeetingOut)
def create_meeting(meeting: MeetingCreate, db: Session = Depends(get_db)):
    db_meeting = Meeting(**meeting.model_dump())
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting


@router.post("/{meeting_id}/upload-audio")
async def upload_audio(meeting_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, f"meeting_{meeting_id}_{file.filename}")
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    meeting.audio_file = file_path
    db.commit()
    return {"message": "Audio uploaded", "path": file_path}


@router.post("/{meeting_id}/transcribe")
async def transcribe_meeting(meeting_id: int, db: Session = Depends(get_db)):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    if not meeting.audio_file:
        raise HTTPException(status_code=400, detail="No audio file uploaded")

    transcript = await transcribe_audio(meeting.audio_file)
    meeting.transcript = transcript
    db.commit()
    return {"transcript": transcript}


@router.post("/{meeting_id}/generate-mom")
async def generate_meeting_mom(meeting_id: int, db: Session = Depends(get_db)):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    if not meeting.transcript:
        raise HTTPException(status_code=400, detail="No transcript available. Transcribe first.")

    mom = await generate_mom(meeting.transcript, meeting.title, meeting.participants or "")
    meeting.mom_text = mom
    db.commit()
    return {"mom": mom}


@router.post("/{meeting_id}/extract-tasks")
async def extract_meeting_tasks(meeting_id: int, db: Session = Depends(get_db)):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    if not meeting.mom_text:
        raise HTTPException(status_code=400, detail="No MOM available. Generate MOM first.")

    tasks_data = await extract_tasks(meeting.mom_text)
    created_tasks = []
    for t in tasks_data:
        member = None
        if t.get("assigned_to") and t["assigned_to"] != "Unassigned":
            member = db.query(Member).filter(Member.name.ilike(f"%{t['assigned_to']}%")).first()

        deadline = None
        if t.get("deadline"):
            try:
                deadline = datetime.fromisoformat(t["deadline"])
            except (ValueError, TypeError):
                pass

        task = Task(
            title=t["title"],
            priority=t.get("priority", "medium"),
            deadline=deadline,
            assigned_to=member.id if member else None,
            meeting_id=meeting_id,
        )
        db.add(task)
        created_tasks.append(t)

    db.commit()
    return {"tasks_created": len(created_tasks), "tasks": created_tasks}


@router.post("/{meeting_id}/paste-transcript")
async def paste_transcript(meeting_id: int, transcript: str = Form(...), db: Session = Depends(get_db)):
    """Manually paste a transcript instead of uploading audio."""
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")

    meeting.transcript = transcript
    db.commit()
    return {"message": "Transcript saved"}
