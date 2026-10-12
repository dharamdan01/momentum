from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from ..database import Base


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300), nullable=False)
    date = Column(DateTime, nullable=False)
    participants = Column(Text)
    transcript = Column(Text)
    mom_text = Column(Text)
    audio_file = Column(String(500))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    tasks = relationship("Task", back_populates="meeting")
