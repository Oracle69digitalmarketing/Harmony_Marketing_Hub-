from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)

    orders = relationship("Order", back_populates="client")


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    status = Column(String, default="Ongoing")
    due_date = Column(Date, nullable=True)

    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)

    client = relationship("Client", back_populates="orders")
