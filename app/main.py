from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

from .database import Base, engine
from .routers import members, meetings, tasks, dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MOMentum - AI-Powered Meeting Intelligence")

app.include_router(members.router)
app.include_router(meetings.router)
app.include_router(tasks.router)
app.include_router(dashboard.router)

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    index_path = os.path.join(STATIC_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()
