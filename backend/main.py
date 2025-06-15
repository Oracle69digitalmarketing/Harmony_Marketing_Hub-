from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

# Routers (modular APIs)
from auth.routes import auth_router
from api.routes import user_router
from api.dashboard import router as dashboard_router
from api.clients import router as client_router
from api.campaigns import router as campaign_router
from api.portfolio import router as portfolio_router

app = FastAPI()

# --- CORS: Allow frontend (Vercel) to connect ---
origins = ["*"]  # Replace "*" with "https://your-vercel-app.vercel.app" in production

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Static files: serve uploaded images ---
os.makedirs("uploaded_images", exist_ok=True)
app.mount("/static", StaticFiles(directory="uploaded_images"), name="static")

# --- Mount API Routes ---
app.include_router(auth_router, prefix="/api")
app.include_router(user_router, prefix="/api")
app.include_router(dashboard_router, prefix="/api")
app.include_router(client_router, prefix="/api")
app.include_router(campaign_router, prefix="/api")
app.include_router(portfolio_router, prefix="/api")

from api.routes import user_router, dashboard_router
app.include_router(dashboard_router, prefix="/api")
