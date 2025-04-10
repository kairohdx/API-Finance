from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.get("/", response_model=list[schemas.Account])
def get_accounts(db: Session = Depends(database.SessionLocal)):
    return db.query(models.Account).all()