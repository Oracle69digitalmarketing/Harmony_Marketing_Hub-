from fastapi import APIRouter, Depends
from auth.auth_handler import decode_access_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = decode_access_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.dependencies import get_current_user
from db.database import get_db
from auth.models import User

router = APIRouter()

@router.get("/dashboard")
def get_dashboard_data(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # You can customize this with real queries
    return {
        "clients": 6,
        "open_jobs": 3,
        "completed_jobs": 12,
        "ai_message": f"Great job, {current_user.business_name or current_user.email.split('@')[0]}! You completed 12 orders this week. Time to follow up and upsell."
    }

@router.get("/ai/growth-planner")
def ai_growth_insights(user=Depends(get_current_user)):
    return {
        "status": "healthy",
        "recommendations": [
            "Engagement is 12% below benchmark – try 9am posts.",
            "Portfolio has low updates – aim for 3 per week."
        ],
        "benchmarks": {
            "avg_open_rate": "18%",
            "your_open_rate": "12%",
            "recommended_posting_time": "9am – 11am"
        }
    }
