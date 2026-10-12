from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from ..database import Base


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(200))
    phone = Column(String(20))
    role = Column(String(50), default="member")
    password_hash = Column(String(200))
    telegram_chat_id = Column(String(100))
    notification_pref = Column(String(20), default="email")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    tasks = relationship("Task", back_populates="assignee")
