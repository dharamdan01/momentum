from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MemberCreate(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    role: str = "member"
    telegram_chat_id: Optional[str] = None
    notification_pref: str = "email"


class MemberOut(BaseModel):
    id: int
    name: str
    email: Optional[str]
    phone: Optional[str]
    role: str
    telegram_chat_id: Optional[str] = None
    notification_pref: Optional[str] = "email"

    model_config = {"from_attributes": True}


class LoginRequest(BaseModel):
    name: str
    password: str


class RegisterRequest(BaseModel):
    name: str
    password: str
    email: Optional[str] = None
    role: Optional[str] = "member"


class LoginResponse(BaseModel):
    token: str
    member: MemberOut


class NotificationPrefUpdate(BaseModel):
    notification_pref: Optional[str] = None
    telegram_chat_id: Optional[str] = None


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


class DashboardStats(BaseModel):
    total_meetings: int
    total_tasks: int
    pending_tasks: int
    in_progress_tasks: int
    completed_tasks: int
    overdue_tasks: int
    members: list[MemberOut]
    upcoming_deadlines: list[TaskOut]
