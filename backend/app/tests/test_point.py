from fastapi.testclient import TestClient
from app.main import app
from app.infrastructure.db.session import SessionLocal, engine
from app.infrastructure.db.base import Base

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_point():
    response = client.post("/points/", json={
        "lat": 10.0,
        "long": 20.0,
        "max_age": 1000,
        "min_age": 500,
        "weight": 1.5,
        "climate": "Tropical"
    })
    assert response.status_code == 200
    assert response.json()["climate"] == "Tropical"

def test_read_point():
    response = client.get("/points/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_read_points():
    response = client.get("/points/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_point():
    response = client.put("/points/1", json={
        "lat": 15.0,
        "long": 25.0,
        "max_age": 1200,
        "min_age": 600,
        "weight": 2.0,
        "climate": "Arid"
    })
    assert response.status_code == 200
    assert response.json()["climate"] == "Arid"

def test_delete_point():
    response = client.delete("/points/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1