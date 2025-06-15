from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.routes import auth_router
from api.routes import user_router

app = FastAPI()

origins = ["*"]  # You can restrict this later

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api")
app.include_router(user_router, prefix="/api")

