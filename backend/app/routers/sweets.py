from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models import Sweet
from ..deps import get_db, get_current_user

router = APIRouter()

@router.get("/")
def get_sweets(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return db.query(Sweet).all()
