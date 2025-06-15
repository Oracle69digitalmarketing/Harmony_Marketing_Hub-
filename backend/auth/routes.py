from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from db.database import SessionLocal
from auth.hash import get_password_hash
from auth.models import User  # or wherever your User model is

auth_router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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

    new_user = User(
        email=user.email,
        hashed_password=hashed_pw,
        business_name=user.businessName
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}
