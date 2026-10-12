from pydantic import BaseModel
from typing import Optional


class NotificationPrefUpdate(BaseModel):
    notification_pref: Optional[str] = None
    telegram_chat_id: Optional[str] = None
