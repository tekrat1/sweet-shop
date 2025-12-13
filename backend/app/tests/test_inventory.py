import sys
import os

# ✅ Ensure backend root is in PYTHONPATH
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_purchase_sweet_unauthorized():
    """
    POST /api/sweets/{id}/purchase should fail without JWT token
    """
    response = client.post("/api/sweets/1/purchase")
    assert response.status_code == 401


def test_restock_sweet_unauthorized():
    """
    POST /api/sweets/{id}/restock should fail without admin token
    """
    response = client.post(
        "/api/sweets/1/restock",
        params={"quantity": 10}
    )
    assert response.status_code == 401
