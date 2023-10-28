from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}

def test_read_item_with_query():
    response = client.get("/items/5?q=test_query")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "test_query"}
