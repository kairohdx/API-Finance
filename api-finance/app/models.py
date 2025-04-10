from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.database import Base

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    amount = Column(Float)
    description = Column(String)
    date = Column(Date)