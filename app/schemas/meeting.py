from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from .task import TaskOut


class MeetingCreate(BaseModel):
    title: str
    date: datetime
    participants: Optional[str] = None


class MeetingOut(BaseModel):
    id: int
    title: str
    date: datetime
    participants: Optional[str]
    transcript: Optional[str]
    mom_text: Optional[str]
    audio_file: Optional[str]
    created_at: datetime
    tasks: list[TaskOut] = []

    model_config = {"from_attributes": True}
