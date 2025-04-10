from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, database

router = APIRouter(prefix="/summary", tags=["Summary"])

@router.get("/")
def get_summary(db: Session = Depends(database.SessionLocal)):
    total = db.query(func.sum(models.Transaction.amount)).scalar()
    return {"total_balance": total}