from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
import logging

from .database import Base, engine
from .routers import members, meetings, tasks, dashboard, auth, notifications

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

_MIGRATIONS = [
    ("members", "password_hash", "VARCHAR(200)"),
    ("members", "telegram_chat_id", "VARCHAR(100)"),
    ("members", "notification_pref", "VARCHAR(20) DEFAULT 'email'"),
]


def run_migrations():
    from sqlalchemy import text, inspect
    with engine.connect() as conn:
        inspector = inspect(engine)
        for table, column, col_type in _MIGRATIONS:
            existing = [c["name"] for c in inspector.get_columns(table)]
            if column not in existing:
                conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}"))
                logger.info(f"Migration: added {table}.{column}")
        conn.commit()


run_migrations()


@asynccontextmanager
async def lifespan(app: FastAPI):
    from .services.scheduler import start_scheduler, stop_scheduler
    start_scheduler()
    yield
    stop_scheduler()


app = FastAPI(title="MOMentum - AI-Powered Meeting Intelligence", lifespan=lifespan)

app.include_router(auth.router)
app.include_router(members.router)
app.include_router(meetings.router)
app.include_router(tasks.router)
app.include_router(dashboard.router)
app.include_router(notifications.router)

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    index_path = os.path.join(STATIC_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()
