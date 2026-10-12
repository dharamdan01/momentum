import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import httpx
import logging

logger = logging.getLogger(__name__)

SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
SMTP_FROM = os.getenv("SMTP_FROM", "")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")


def send_email(to_email: str, subject: str, body: str) -> bool:
    if not all([SMTP_HOST, SMTP_USER, SMTP_PASS, to_email]):
        logger.warning("Email not configured or no recipient — skipping")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_FROM or SMTP_USER
    msg["To"] = to_email

    html = f"""
    <div style="font-family:Inter,system-ui,sans-serif;max-width:560px;margin:0 auto;padding:24px;">
      <div style="background:linear-gradient(135deg,#6366f1,#8b5cf6);padding:16px 24px;border-radius:12px 12px 0 0;">
        <h1 style="color:white;font-size:18px;margin:0;">MOMentum</h1>
      </div>
      <div style="background:#fff;border:1px solid #e4e4e8;border-top:none;padding:24px;border-radius:0 0 12px 12px;">
        {body}
        <hr style="border:none;border-top:1px solid #e4e4e8;margin:20px 0;">
        <p style="color:#8b8fa3;font-size:12px;margin:0;">
          Sent by MOMentum &mdash; AI-Powered Meeting Intelligence
        </p>
      </div>
    </div>
    """
    msg.attach(MIMEText(body, "plain"))
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(msg["From"], [to_email], msg.as_string())
        logger.info(f"Email sent to {to_email}: {subject}")
        return True
    except Exception as e:
        logger.error(f"Email failed for {to_email}: {e}")
        return False


async def send_telegram(chat_id: str, message: str) -> bool:
    if not TELEGRAM_BOT_TOKEN or not chat_id:
        logger.warning("Telegram not configured or no chat_id — skipping")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, json=payload, timeout=10)
            if resp.status_code == 200:
                logger.info(f"Telegram sent to {chat_id}")
                return True
            logger.error(f"Telegram API error: {resp.status_code} {resp.text}")
            return False
    except Exception as e:
        logger.error(f"Telegram failed for {chat_id}: {e}")
        return False


async def notify_member(member, subject: str, body: str, telegram_text: str | None = None):
    """Send notification to a member via their preferred channel."""
    pref = getattr(member, "notification_pref", "email") or "email"

    if pref in ("email", "all") and member.email:
        send_email(member.email, subject, body)

    if pref in ("telegram", "all"):
        chat_id = getattr(member, "telegram_chat_id", None)
        if chat_id:
            await send_telegram(chat_id, telegram_text or body)


async def notify_task_reminder(member, task) -> bool:
    """Send a task deadline reminder to a member."""
    subject = f"Reminder: {task.title}"

    deadline_str = task.deadline.strftime("%d %b %Y") if task.deadline else "No deadline"
    body = (
        f"<h3>Task Reminder</h3>"
        f"<p><strong>{task.title}</strong></p>"
        f"<p>Deadline: {deadline_str}</p>"
        f"<p>Status: {task.status.value if hasattr(task.status, 'value') else task.status}</p>"
        f"<p>Please update the task status in MOMentum.</p>"
    )
    telegram_text = (
        f"<b>Task Reminder</b>\n"
        f"{task.title}\n"
        f"Deadline: {deadline_str}\n"
        f"Status: {task.status.value if hasattr(task.status, 'value') else task.status}"
    )

    await notify_member(member, subject, body, telegram_text)
    return True


async def notify_overdue(member, task) -> bool:
    """Send an overdue alert to a member."""
    subject = f"OVERDUE: {task.title}"

    deadline_str = task.deadline.strftime("%d %b %Y") if task.deadline else "No deadline"
    body = (
        f"<h3 style='color:#dc2626;'>Overdue Task</h3>"
        f"<p><strong>{task.title}</strong></p>"
        f"<p>Deadline was: {deadline_str}</p>"
        f"<p>This task is now overdue. Please take action.</p>"
    )
    telegram_text = (
        f"<b>OVERDUE</b>\n"
        f"{task.title}\n"
        f"Deadline was: {deadline_str}\n"
        f"Please take action immediately."
    )

    await notify_member(member, subject, body, telegram_text)
    return True


async def notify_management_summary(manager, summary: list[dict]) -> bool:
    """Send a task summary to management."""
    subject = "MOMentum — Task Status Summary"

    rows = ""
    for s in summary:
        rows += (
            f"<tr>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;'>{s['name']}</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;text-align:center;'>{s['pending']}</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;text-align:center;'>{s['in_progress']}</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;text-align:center;'>{s['completed']}</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;text-align:center;color:#dc2626;'>{s['overdue']}</td>"
            f"</tr>"
        )

    body = (
        f"<h3>Task Status Summary</h3>"
        f"<table style='width:100%;border-collapse:collapse;font-size:13px;'>"
        f"<tr style='background:#f7f7f8;'>"
        f"<th style='padding:8px;text-align:left;'>Member</th>"
        f"<th style='padding:8px;text-align:center;'>Pending</th>"
        f"<th style='padding:8px;text-align:center;'>In Progress</th>"
        f"<th style='padding:8px;text-align:center;'>Completed</th>"
        f"<th style='padding:8px;text-align:center;'>Overdue</th>"
        f"</tr>{rows}</table>"
    )

    lines = ["<b>Task Status Summary</b>\n"]
    for s in summary:
        lines.append(f"{s['name']}: {s['pending']}P / {s['in_progress']}IP / {s['completed']}C / {s['overdue']}OD")
    telegram_text = "\n".join(lines)

    await notify_member(manager, subject, body, telegram_text)
    return True
