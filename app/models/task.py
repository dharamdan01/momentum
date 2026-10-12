from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import enum

from ..database import Base


class TaskStatus(str, enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    OVERDUE = "overdue"


class TaskPriority(str, enum.Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    description = Column(Text)
    status = Column(SqlEnum(TaskStatus), default=TaskStatus.PENDING)
    priority = Column(SqlEnum(TaskPriority), default=TaskPriority.MEDIUM)
    deadline = Column(DateTime)
    assigned_to = Column(Integer, ForeignKey("members.id"))
    meeting_id = Column(Integer, ForeignKey("meetings.id"))
    reminder_sent = Column(Integer, default=0)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    assignee = relationship("Member", back_populates="tasks")
    meeting = relationship("Meeting", back_populates="tasks")
