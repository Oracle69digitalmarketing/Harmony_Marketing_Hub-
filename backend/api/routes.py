from fastapi import APIRouter
from pydantic import BaseModel

user_router = APIRouter()

class BusinessProfile(BaseModel):
    business_name: str
    industry: str
    target_audience: str
    main_services: list[str]

@user_router.get("/profile")
def get_profile():
    return {"business_name": "Harmony Sample", "industry": "Retail", "target_audience": "Shoppers", "main_services": ["Clothing", "Accessories"]}

@user_router.put("/profile")
def update_profile(profile: BusinessProfile):
    return {"message": "Profile updated", "data": profile}
