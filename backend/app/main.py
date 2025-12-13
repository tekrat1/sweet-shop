from fastapi import FastAPI
from app.routers import auth, sweets, inventory

app = FastAPI(
    title="Sweet Shop Management System",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(sweets.router)
app.include_router(inventory.router)
