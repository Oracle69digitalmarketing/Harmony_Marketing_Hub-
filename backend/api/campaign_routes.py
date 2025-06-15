from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from auth.dependencies import get_current_user
from models.campaign import Campaign
from pydantic import BaseModel

router = APIRouter()

class CampaignInput(BaseModel):
    title: str
    subject: str
    body: str

@router.post("/campaigns")
def save_campaign(data: CampaignInput, db: Session = Depends(get_db), user=Depends(get_current_user)):
    campaign = Campaign(**data.dict(), user_id=user.id)
    db.add(campaign)
    db.commit()
    return {"message": "Campaign saved"}
