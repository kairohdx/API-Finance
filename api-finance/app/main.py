from fastapi import FastAPI
from app import mock_data, models, database
from app.routes import accounts, transactions, summary

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="API Finance")

app.include_router(accounts.router)
app.include_router(transactions.router)
app.include_router(summary.router)

@app.on_event("startup")
def startup_event():
    mock_data.create_mock_data()