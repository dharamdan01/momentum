from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Member, Task, TaskStatus
from ..schemas import NotificationPrefUpdate, MemberOut
from ..services.notifications import (
    notify_member,
    notify_management_summary,
    send_email,
    send_telegram,
)
from ..services.reminder import get_member_tasks_summary, check_overdue_tasks, get_upcoming_deadlines
from ..services.auth import require_auth

router = APIRouter(prefix="/api/notifications", tags=["notifications"])


@router.patch("/preferences", response_model=MemberOut)
def update_preferences(
    update: NotificationPrefUpdate,
    user: Member = Depends(require_auth),
    db: Session = Depends(get_db),
):
    if update.notification_pref is not None:
        user.notification_pref = update.notification_pref
    if update.telegram_chat_id is not None:
        user.telegram_chat_id = update.telegram_chat_id
    db.commit()
    db.refresh(user)
    return user


@router.post("/test")
async def send_test_notification(user: Member = Depends(require_auth)):
    subject = "Test Notification from MOMentum"
    body = "<p>This is a test notification. If you received this, your notifications are working!</p>"
    telegram_text = "<b>Test Notification</b>\nMOMentum notifications are working!"

    await notify_member(user, subject, body, telegram_text)
    return {"message": "Test notification sent"}


@router.post("/send-summary")
async def trigger_summary(db: Session = Depends(get_db)):
    """Manually trigger a summary notification to all managers."""
    managers = db.query(Member).filter(Member.role == "management").all()
    if not managers:
        raise HTTPException(status_code=404, detail="No management members found")

    summary = get_member_tasks_summary(db)
    for manager in managers:
        await notify_management_summary(manager, summary)

    return {"message": f"Summary sent to {len(managers)} manager(s)"}


@router.post("/send-reminders")
async def trigger_reminders(db: Session = Depends(get_db)):
    """Manually trigger overdue and upcoming deadline reminders."""
    from ..services.scheduler import run_reminder_cycle
    await run_reminder_cycle()
    return {"message": "Reminder cycle triggered"}


@router.get("/status")
def notification_status():
    """Check which notification channels are configured."""
    from ..services.notifications import SMTP_HOST, TELEGRAM_BOT_TOKEN
    return {
        "email_configured": bool(SMTP_HOST),
        "telegram_configured": bool(TELEGRAM_BOT_TOKEN),
    }
