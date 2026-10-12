from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import logging

from .config import UPLOAD_DIR
from .database import Base, engine
from .migrations import run_migrations
from .routers import members, meetings, tasks, dashboard, auth, notifications

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)
run_migrations(engine)


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

STATIC_DIR = str(UPLOAD_DIR.parent / "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    index_path = UPLOAD_DIR.parent / "static" / "index.html"
    return index_path.read_text(encoding="utf-8")
