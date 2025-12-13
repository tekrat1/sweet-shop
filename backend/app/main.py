from fastapi import FastAPI
from app.routers import auth, sweets, inventory

app = FastAPI()

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(sweets.router, prefix="/api/sweets", tags=["Sweets"])
app.include_router(inventory.router, prefix="/api/inventory", tags=["Inventory"])
