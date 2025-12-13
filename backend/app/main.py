from fastapi import FastAPI
from app.routers import auth, sweets, inventory

app = FastAPI()

app.include_router(auth.router)
app.include_router(sweets.router)
app.include_router(inventory.router)
