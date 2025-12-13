from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user, admin_only
from app.models import Sweet
from app.schemas import SweetCreate   # ✅ FIXED IMPORT

router = APIRouter(
    prefix="/api/sweets",
    tags=["Sweets"]
)

# --------------------------------------------------
# GET ALL SWEETS (LOGGED IN USERS)
# --------------------------------------------------
@router.get("/", status_code=status.HTTP_200_OK)
def get_sweets(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return db.query(Sweet).all()


# --------------------------------------------------
# SEARCH SWEETS
# --------------------------------------------------
@router.get("/search", status_code=status.HTTP_200_OK)
def search_sweets(
    name: str | None = None,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    query = db.query(Sweet)

    if name:
        query = query.filter(Sweet.name.ilike(f"%{name}%"))

    if category:
        query = query.filter(Sweet.category.ilike(f"%{category}%"))

    if min_price is not None:
        query = query.filter(Sweet.price >= min_price)

    if max_price is not None:
        query = query.filter(Sweet.price <= max_price)

    return query.all()


# --------------------------------------------------
# CREATE SWEET (ADMIN ONLY)
# --------------------------------------------------
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_sweet(
    sweet: SweetCreate,
    db: Session = Depends(get_db),
    admin = Depends(admin_only)   # ✅ CLEAN ADMIN CHECK
):
    new_sweet = Sweet(
        name=sweet.name,
        category=sweet.category,
        price=sweet.price,
        quantity=sweet.quantity
    )

    db.add(new_sweet)
    db.commit()
    db.refresh(new_sweet)

    return new_sweet


# --------------------------------------------------
# UPDATE SWEET (ADMIN ONLY)
# --------------------------------------------------
@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_sweet(
    id: int,
    sweet: SweetCreate,
    db: Session = Depends(get_db),
    admin = Depends(admin_only)   # ✅ CLEAN ADMIN CHECK
):
    db_sweet = db.query(Sweet).filter(Sweet.id == id).first()

    if not db_sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    db_sweet.name = sweet.name
    db_sweet.category = sweet.category
    db_sweet.price = sweet.price
    db_sweet.quantity = sweet.quantity

    db.commit()
    db.refresh(db_sweet)

    return db_sweet


# --------------------------------------------------
# DELETE SWEET (ADMIN ONLY)
# --------------------------------------------------
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_sweet(
    id: int,
    db: Session = Depends(get_db),
    admin = Depends(admin_only)   # ✅ CLEAN ADMIN CHECK
):
    sweet = db.query(Sweet).filter(Sweet.id == id).first()

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    db.delete(sweet)
    db.commit()

    return {"message": "Sweet deleted"}
