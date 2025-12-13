import sys
import os

# ✅ FIX: ensure backend root is in PYTHONPATH
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_sweets_unauthorized():
    """
    GET /api/sweets should fail without JWT token
    """
    response = client.get("/api/sweets/")
    assert response.status_code == 401


def test_create_sweet_unauthorized():
    """
    POST /api/sweets should fail without admin token
    """
    response = client.post(
        "/api/sweets/",
        json={
            "name": "Ladoo",
            "category": "Indian",
            "price": 10.0,
            "quantity": 100
        }
    )
    assert response.status_code == 401
