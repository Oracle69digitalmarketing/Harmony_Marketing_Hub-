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

@router.get("/dashboard-summary")
def dashboard_summary(user=Depends(get_current_user)):
    return {
        "kpis": {
            "leads": 10,
            "orders": 5,
            "portfolio": 7
        },
        "insights": [
            "Try posting 2 more items this week.",
            "Run an email campaign – your last one was 14 days ago."
        ]
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
