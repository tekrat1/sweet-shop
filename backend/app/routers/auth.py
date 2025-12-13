from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register():
    return {"message": "register works"}

@router.post("/login")
def login():
    return {"message": "login works"}
