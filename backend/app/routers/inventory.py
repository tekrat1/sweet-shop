from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user, admin_only
from app.models import Sweet

# ❌ NO router prefix here
router = APIRouter(tags=["Inventory"])


@router.post("/api/sweets/{id}/purchase", status_code=status.HTTP_200_OK)
def purchase_sweet(
    id: int,
    quantity: int = 1,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if quantity <= 0:
        raise HTTPException(400, "Quantity must be greater than 0")

    sweet = db.query(Sweet).filter(Sweet.id == id).first()
    if not sweet:
        raise HTTPException(404, "Sweet not found")

    if sweet.quantity < quantity:
        raise HTTPException(400, "Not enough stock available")

    sweet.quantity -= quantity
    db.commit()

    return {
        "message": "Purchase successful",
        "remaining_stock": sweet.quantity
    }


@router.post("/api/sweets/{id}/restock", status_code=status.HTTP_200_OK)
def restock_sweet(
    id: int,
    quantity: int,
    db: Session = Depends(get_db),
    admin=Depends(admin_only)
):
    if quantity <= 0:
        raise HTTPException(400, "Quantity must be greater than 0")

    sweet = db.query(Sweet).filter(Sweet.id == id).first()
    if not sweet:
        raise HTTPException(404, "Sweet not found")

    sweet.quantity += quantity
    db.commit()

    return {
        "message": "Restock successful",
        "new_stock": sweet.quantity
    }
