from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
import uuid

from db.database import get_db
from auth.hash import get_password_hash
from auth.models import User
from utils.email import send_verification_email

auth_router = APIRouter()

class RegisterUser(BaseModel):
    email: EmailStr
    password: str
    businessName: str

@auth_router.post("/register", status_code=201)
def register_user(user: RegisterUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = get_password_hash(user.password)
    token = str(uuid.uuid4())

    new_user = User(
        email=user.email,
        hashed_password=hashed_pw,
        business_name=user.businessName,
        verification_token=token,
        verified=False
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    send_verification_email(user.email, token)

    return {"message": "Check your email to verify your account"}
