from pydantic import BaseModel, EmailStr


# --------------------------------------------------
# AUTH SCHEMAS
# --------------------------------------------------
class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# --------------------------------------------------
# SWEET SCHEMAS
# --------------------------------------------------
class SweetCreate(BaseModel):
    name: str
    category: str
    price: float
    quantity: int
