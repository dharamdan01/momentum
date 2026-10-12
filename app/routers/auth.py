from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Member
from ..schemas import LoginRequest, LoginResponse, RegisterRequest, MemberOut
from ..services.auth import hash_password, verify_password, create_token, require_auth

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=LoginResponse)
def register(req: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(Member).filter(Member.name.ilike(req.name)).first()
    if existing and existing.password_hash:
        raise HTTPException(status_code=400, detail="User already registered")

    if existing:
        existing.password_hash = hash_password(req.password)
        if req.email:
            existing.email = req.email
        db.commit()
        db.refresh(existing)
        member = existing
    else:
        member = Member(
            name=req.name,
            email=req.email,
            role=req.role or "member",
            password_hash=hash_password(req.password),
        )
        db.add(member)
        db.commit()
        db.refresh(member)

    token = create_token(member.id, member.role)
    return LoginResponse(token=token, member=MemberOut.model_validate(member))


@router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.name.ilike(req.name)).first()
    if not member or not member.password_hash:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not verify_password(req.password, member.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(member.id, member.role)
    return LoginResponse(token=token, member=MemberOut.model_validate(member))


@router.get("/me", response_model=MemberOut)
def get_me(user: Member = Depends(require_auth)):
    return user
