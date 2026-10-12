from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Session
from ..models import Task, TaskStatus, Member


def check_overdue_tasks(db: Session) -> list[dict]:
    """Find tasks that are past their deadline and not completed."""
    now = datetime.utcnow()
    overdue = (
        db.query(Task)
        .filter(Task.deadline < now, Task.status != TaskStatus.COMPLETED)
        .all()
    )
    alerts = []
    for task in overdue:
        if task.status != TaskStatus.OVERDUE:
            task.status = TaskStatus.OVERDUE
        alerts.append(
            {
                "task_id": task.id,
                "title": task.title,
                "assignee": task.assignee.name if task.assignee else "Unassigned",
                "deadline": task.deadline.isoformat(),
                "days_overdue": (now - task.deadline).days,
            }
        )
    db.commit()
    return alerts


def get_upcoming_deadlines(db: Session, days: int = 3) -> list[dict]:
    """Get tasks with deadlines in the next N days."""
    now = datetime.utcnow()
    cutoff = now + timedelta(days=days)
    upcoming = (
        db.query(Task)
        .filter(
            Task.deadline >= now,
            Task.deadline <= cutoff,
            Task.status != TaskStatus.COMPLETED,
        )
        .all()
    )
    return [
        {
            "task_id": t.id,
            "title": t.title,
            "assignee": t.assignee.name if t.assignee else "Unassigned",
            "deadline": t.deadline.isoformat(),
            "days_left": (t.deadline - now).days,
        }
        for t in upcoming
    ]


def get_member_tasks_summary(db: Session) -> list[dict]:
    """Get task summary per member for management dashboard."""
    members = db.query(Member).all()
    summary = []
    for member in members:
        tasks = db.query(Task).filter(Task.assigned_to == member.id).all()
        summary.append(
            {
                "member_id": member.id,
                "name": member.name,
                "total": len(tasks),
                "pending": sum(1 for t in tasks if t.status == TaskStatus.PENDING),
                "in_progress": sum(
                    1 for t in tasks if t.status == TaskStatus.IN_PROGRESS
                ),
                "completed": sum(
                    1 for t in tasks if t.status == TaskStatus.COMPLETED
                ),
                "overdue": sum(1 for t in tasks if t.status == TaskStatus.OVERDUE),
            }
        )
    return summary
