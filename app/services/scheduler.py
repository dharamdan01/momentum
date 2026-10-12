import logging
from datetime import datetime, timezone, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from ..config import REMINDER_INTERVAL_HOURS, REMINDER_INITIAL_DELAY_MINUTES
from ..database import SessionLocal
from ..models import Task, TaskStatus, Member
from .notifications import notify_task_reminder, notify_overdue, notify_management_summary
from .reminder import check_overdue_tasks, get_upcoming_deadlines, get_member_tasks_summary

logger = logging.getLogger(__name__)

scheduler = AsyncIOScheduler()


async def run_reminder_cycle():
    logger.info("Running reminder cycle...")
    db = SessionLocal()
    try:
        overdue_alerts = check_overdue_tasks(db)
        for alert in overdue_alerts:
            task = db.query(Task).filter(Task.id == alert["task_id"]).first()
            if task and task.assignee:
                await notify_overdue(task.assignee, task)

        upcoming = get_upcoming_deadlines(db, days=3)
        for item in upcoming:
            task = db.query(Task).filter(Task.id == item["task_id"]).first()
            if task and task.assignee and not task.reminder_sent:
                await notify_task_reminder(task.assignee, task)
                task.reminder_sent = 1
                db.commit()

        managers = db.query(Member).filter(Member.role == "management").all()
        if managers:
            summary = get_member_tasks_summary(db)
            for manager in managers:
                await notify_management_summary(manager, summary)

        logger.info(f"Reminder cycle done: {len(overdue_alerts)} overdue, {len(upcoming)} upcoming")
    except Exception as e:
        logger.error(f"Reminder cycle error: {e}")
    finally:
        db.close()


def start_scheduler():
    scheduler.add_job(
        run_reminder_cycle,
        trigger=IntervalTrigger(hours=REMINDER_INTERVAL_HOURS),
        id="reminder_cycle",
        replace_existing=True,
        next_run_time=datetime.now(timezone.utc) + timedelta(minutes=REMINDER_INITIAL_DELAY_MINUTES),
    )
    scheduler.start()
    logger.info(f"Scheduler started — reminders every {REMINDER_INTERVAL_HOURS} hours")


def stop_scheduler():
    if scheduler.running:
        scheduler.shutdown(wait=False)
        logger.info("Scheduler stopped")
