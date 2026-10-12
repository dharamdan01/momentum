from pydantic import BaseModel
from typing import Optional

from .member import MemberOut


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
