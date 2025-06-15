from fastapi import APIRouter, UploadFile, Form, File, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from auth.dependencies import get_current_user
from models.portfolio import PortfolioItem
import uuid
import shutil

router = APIRouter()

@router.post("/portfolio/upload")
def upload_design(
    image: UploadFile = File(...),
    design_name: str = Form(...),
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    # Save image locally or to cloud
    filename = f"{uuid.uuid4().hex}_{image.filename}"
    path = f"static/uploads/{filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Simulate AI tagging (mocked)
    tags = "Ankara,Fashion,Nigeria"
    category = "Tailoring"
    caption = f"{design_name} — handcrafted with love and style."

    item = PortfolioItem(
        image_url=f"/static/uploads/{filename}",
        design_name=design_name,
        tags=tags,
        category=category,
        caption=caption,
        user_id=user.id
    )
    db.add(item)
    db.commit()
    db.refresh(item)

    return item
