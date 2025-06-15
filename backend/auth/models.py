from pydantic import BaseModel

class UserSignup(BaseModel):
    email: str
    password: str
    role: str

class UserLogin(BaseModel):
    email: str
    password: str

from sqlalchemy import Column, String, Boolean
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    business_name = Column(String, nullable=True)

    verified = Column(Boolean, default=False)
    verification_token = Column(String, unique=True, nullable=True)
