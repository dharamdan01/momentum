from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from .member import MemberOut


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"
    priority: str = "medium"
    deadline: Optional[datetime] = None
    assigned_to: Optional[int] = None
    meeting_id: Optional[int] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    deadline: Optional[datetime] = None
    assigned_to: Optional[int] = None


class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    priority: str
    deadline: Optional[datetime]
    assigned_to: Optional[int]
    meeting_id: Optional[int]
    assignee: Optional[MemberOut] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
