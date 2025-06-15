from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from auth.dependencies import get_current_user

router = APIRouter()

@router.get("/growth")
def get_growth_insights(db: Session = Depends(get_db), user=Depends(get_current_user)):
    # Simulated metrics - later query real campaign + order data
    return {
        "client_count": 12,
        "completed_jobs": 28,
        "avg_lead_time": "3.5 days",
        "predicted_orders": 7,
        "recommendation": "🧠 This week: Follow up with past clients and run a WhatsApp promo for repeat orders."
    }
