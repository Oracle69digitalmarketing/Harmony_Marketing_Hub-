from fastapi import APIRouter, HTTPException, Depends
from uuid import uuid4
from .auth_handler import hash_password, verify_password, create_access_token, decode_access_token
from .models import UserSignup, UserLogin

auth_router = APIRouter()
fake_users_db = {}

@auth_router.post("/register")
def register(user: UserSignup):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered.")
    fake_users_db[user.email] = {
        "id": str(uuid4()),
        "email": user.email,
        "password": hash_password(user.password),
        "role": user.role
    }
    return {"message": "User registered successfully"}

@auth_router.post("/login")
def login(user: UserLogin):
    stored_user = fake_users_db.get(user.email)
    if not stored_user or not verify_password(user.password, stored_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email, "role": stored_user["role"]})
    return {"token": token, "user": {"email": stored_user["email"], "role": stored_user["role"]}}

token = create_access_token({"sub": db_user.email, "user_id": db_user.id, "role": db_user.role})