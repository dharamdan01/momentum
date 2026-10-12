import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Database
DB_PATH = BASE_DIR / "data.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

# Upload storage
UPLOAD_DIR = BASE_DIR / "app" / "uploads"

# AI APIs
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# JWT Auth
JWT_SECRET = os.getenv("JWT_SECRET", "momentum-secret-change-in-production")
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_HOURS = 72

# SMTP Email
SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
SMTP_FROM = os.getenv("SMTP_FROM", "")

# Telegram Bot
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

# Scheduler
REMINDER_INTERVAL_HOURS = 6
REMINDER_INITIAL_DELAY_MINUTES = 1
