from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from auth.dependencies import get_current_user

router = APIRouter()

class CopyRequest(BaseModel):
    type: str  # "email", "caption", "ad"
    topic: str
    tone: Optional[str] = "friendly"
    audience: Optional[str] = "customers"
    cta: Optional[str] = "Learn more"

@router.post("/copywriter")
def generate_copy(request: CopyRequest, user=Depends(get_current_user)):
    # Simulate GPT response
    sample_output = {
        "email": f"Hi there 👋\n\nCheck out our latest offer on {request.topic}. It's built just for {request.audience}. {request.cta}!",
        "caption": f"🔥 New drop: {request.topic}! Perfect for {request.audience}. {request.cta} #HarmonyHub",
        "ad": f"{request.topic} — made for {request.audience}. {request.cta} today!"
    }
    return {
        "generated": sample_output.get(request.type, f"{request.topic} is amazing! {request.cta}")
    }
