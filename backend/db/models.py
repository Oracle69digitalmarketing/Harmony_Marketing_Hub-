from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BusinessProfile(Base):
    __tablename__ = "business_profiles"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    business_name = Column(String)
    industry = Column(String)
    target_audience = Column(String)
    main_services = Column(String)  # comma-separated for simplicity

    user = relationship("User", backref="profile")

from .database import Base, engine
from .models import User, BusinessProfile

print("Creating tables...")
Base.metadata.create_all(bind=engine)

from sqlalchemy import Column, String, DateTime
from uuid import uuid4
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)