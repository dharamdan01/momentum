from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timezone, timedelta

from ..database import get_db
from ..models import Meeting, Task, Member, TaskStatus
from ..schemas import DashboardStats, MemberOut, TaskOut
from ..services.reminder import check_overdue_tasks, get_upcoming_deadlines, get_member_tasks_summary

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("/stats", response_model=DashboardStats)
def get_stats(db: Session = Depends(get_db)):
    check_overdue_tasks(db)

    total_meetings = db.query(Meeting).count()
    all_tasks = db.query(Task).all()
    members = db.query(Member).all()

    now = datetime.now(timezone.utc)
    cutoff = now + timedelta(days=7)
    upcoming = (
        db.query(Task)
        .filter(Task.deadline >= now, Task.deadline <= cutoff, Task.status != TaskStatus.COMPLETED)
        .order_by(Task.deadline.asc())
        .limit(10)
        .all()
    )

    return DashboardStats(
        total_meetings=total_meetings,
        total_tasks=len(all_tasks),
        pending_tasks=sum(1 for t in all_tasks if t.status == TaskStatus.PENDING),
        in_progress_tasks=sum(1 for t in all_tasks if t.status == TaskStatus.IN_PROGRESS),
        completed_tasks=sum(1 for t in all_tasks if t.status == TaskStatus.COMPLETED),
        overdue_tasks=sum(1 for t in all_tasks if t.status == TaskStatus.OVERDUE),
        members=members,
        upcoming_deadlines=upcoming,
    )


@router.get("/alerts")
def get_alerts(db: Session = Depends(get_db)):
    overdue = check_overdue_tasks(db)
    upcoming = get_upcoming_deadlines(db, days=3)
    return {"overdue": overdue, "upcoming_deadlines": upcoming}


@router.get("/member-summary")
def member_summary(db: Session = Depends(get_db)):
    return get_member_tasks_summary(db)
