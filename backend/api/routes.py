from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import BusinessProfile
from auth.auth_handler import decode_access_token

def get_current_user(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    user = decode_access_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from pydantic import BaseModel

class BusinessProfileIn(BaseModel):
    business_name: str
    industry: str
    target_audience: str
    main_services: str  # Comma-separated for now

@user_router.get("/profile")
def get_profile(user=Depends(get_current_user), db: Session = Depends(get_db)):
    profile = db.query(BusinessProfile).filter(BusinessProfile.user_id == user["sub"]).first()
    if not profile:
        return {"message": "No profile found"}
    return {
        "business_name": profile.business_name,
        "industry": profile.industry,
        "target_audience": profile.target_audience,
        "main_services": profile.main_services
    }

@user_router.put("/profile")
def update_profile(profile: BusinessProfileIn, user=Depends(get_current_user), db: Session = Depends(get_db)):
    existing = db.query(BusinessProfile).filter(BusinessProfile.user_id == user["sub"]).first()
    if existing:
        existing.business_name = profile.business_name
        existing.industry = profile.industry
        existing.target_audience = profile.target_audience
        existing.main_services = profile.main_services
    else:
        existing = BusinessProfile(
            user_id=user["sub"],
            **profile.dict()
        )
        db.add(existing)
    db.commit()
    return {"message": "Profile saved"}

@user_router.get("/profile")
def get_profile(user=Depends(get_current_user)):
    return {
        "email": user["sub"],
        "role": user["role"],
        "message": "This is a protected profile endpoint."
    }
