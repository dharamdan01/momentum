from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Member
from ..schemas import MemberCreate, MemberOut

router = APIRouter(prefix="/api/members", tags=["members"])


@router.get("/", response_model=list[MemberOut])
def list_members(db: Session = Depends(get_db)):
    return db.query(Member).all()


@router.post("/", response_model=MemberOut)
def create_member(member: MemberCreate, db: Session = Depends(get_db)):
    data = member.model_dump()
    data.pop("password", None)
    db_member = Member(**data)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


@router.get("/{member_id}", response_model=MemberOut)
def get_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@router.patch("/{member_id}", response_model=MemberOut)
def update_member(member_id: int, update: MemberCreate, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    data = update.model_dump(exclude_unset=True)
    data.pop("password", None)
    for field, value in data.items():
        setattr(member, field, value)
    db.commit()
    db.refresh(member)
    return member


@router.delete("/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    db.delete(member)
    db.commit()
    return {"message": "Member deleted"}
