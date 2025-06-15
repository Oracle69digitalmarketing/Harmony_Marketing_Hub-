from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env

# Use DATABASE_URL from .env or fallback to local
DB_URL = os.getenv("DB_URL", "postgresql://postgres:yourpassword@localhost/harmony_db")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
