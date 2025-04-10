from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_accounts():
    response = client.get("/accounts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_transactions():
    response = client.get("/transactions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_summary():
    response = client.get("/summary/")
    assert response.status_code == 200
    assert "total_balance" in response.json()
    