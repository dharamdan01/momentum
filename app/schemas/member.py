from pydantic import BaseModel
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
