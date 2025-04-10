from pydantic import BaseModel
from datetime import date

class AccountBase(BaseModel):
    name: str

class Account(AccountBase):
    id: int
    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    account_id: int
    amount: float
    description: str
    date: date

class Transaction(TransactionBase):
    id: int
    class Config:
        orm_mode = True