from pydantic import BaseModel

class UserSignup(BaseModel):
    email: str
    password: str
    role: str

class UserLogin(BaseModel):
    email: str
    password: str

from sqlalchemy import Boolean, Column, String

verified = Column(Boolean, default=False)
verification_token = Column(String, nullable=True, unique=True)
