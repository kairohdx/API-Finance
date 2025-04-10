from app.database import SessionLocal
from app import models
from datetime import date, timedelta
import random

def create_mock_data():
    db = SessionLocal()
    if db.query(models.Account).count() == 0:
        accounts = ["Itaú", "Bradesco", "PicPay", "MercadoPago"]
        for acc in accounts:
            db.add(models.Account(name=acc))
        db.commit()

    if db.query(models.Transaction).count() == 0:
        account_ids = [a.id for a in db.query(models.Account).all()]
        for _ in range(100):
            db.add(models.Transaction(
                account_id=random.choice(account_ids),
                amount=round(random.uniform(-500, 2000), 2),
                description=random.choice(["Spotify", "Aluguel", "Salário", "Investimento"]),
                date=date.today() - timedelta(days=random.randint(0, 90))
            ))
        db.commit()
    db.close()