from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/", response_model=list[schemas.Transaction])
def get_transactions(db: Session = Depends(database.SessionLocal)):
    return db.query(models.Transaction).all()