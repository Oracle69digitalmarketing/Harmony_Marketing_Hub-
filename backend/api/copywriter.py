from fastapi import APIRouter, Depends
from pydantic import BaseModel
from auth.auth_handler import get_current_user
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

router = APIRouter()

class CopyInput(BaseModel):
    content_type: str
    tone: str
    message: str
    target_audience: str
    cta: str

@router.post("/generate-copy")
def generate_copy(data: CopyInput, user=Depends(get_current_user)):
    prompt = (
        f"Write a {data.content_type} in a {data.tone} tone. "
        f"Message: {data.message}. Audience: {data.target_audience}. "
        f"Call to Action: {data.cta}"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"copy": response.choices[0].message.content.strip()}