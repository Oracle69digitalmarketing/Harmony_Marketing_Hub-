from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.dependencies import get_current_user
from db.database import get_db
from models.client import Client, Order
from pydantic import BaseModel
from typing import List
from datetime import date

router = APIRouter()

# Pydantic models
class ClientCreate(BaseModel):
    name: str
    phone: str = None
    email: str = None

class OrderCreate(BaseModel):
    title: str
    due_date: date = None
    client_id: int

@router.get("/clients", response_model=List[ClientCreate])
def get_clients(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Client).filter(Client.user_id == user.id).all()

@router.post("/clients")
def create_client(client: ClientCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_client = Client(**client.dict(), user_id=user.id)
    db.add(new_client)
    db.commit()
    return {"message": "Client created"}

@router.post("/orders")
def create_order(order: OrderCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_order = Order(**order.dict(), user_id=user.id)
    db.add(new_order)
    db.commit()
    return {"message": "Order created"}
