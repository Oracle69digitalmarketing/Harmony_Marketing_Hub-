from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import uuid4

auth_router = APIRouter()

users = {}  # Mock DB

class UserSignup(BaseModel):
    email: str
    password: str
    role: str

@auth_router.post("/register")
def register(user: UserSignup):
    if user.email in users:
        raise HTTPException(status_code=400, detail="Email already registered.")
    users[user.email] = {
        "id": str(uuid4()),
        "email": user.email,
        "password": user.password,  # Hash later!
        "role": user.role
    }
    return {"message": "User registered."}

@auth_router.post("/login")
def login(user: UserSignup):
    if user.email not in users or users[user.email]["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    return {"token": "mock-jwt-token", "user": users[user.email]}
