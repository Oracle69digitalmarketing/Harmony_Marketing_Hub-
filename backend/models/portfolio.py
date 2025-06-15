from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime

class PortfolioItem(Base):
    __tablename__ = "portfolio_items"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=False)
    design_name = Column(String, nullable=False)
    tags = Column(String)           # comma-separated
    category = Column(String)
    caption = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(String, ForeignKey("users.id"), nullable=False)
