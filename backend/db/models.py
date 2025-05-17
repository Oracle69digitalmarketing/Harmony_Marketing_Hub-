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