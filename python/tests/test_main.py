from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to agriMarketWatch API"}

def test_read_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "API is up and running"}