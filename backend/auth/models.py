from pydantic import BaseModel

class UserSignup(BaseModel):
    email: str
    password: str
    role: str

class UserLogin(BaseModel):
    email: str
    password: str
