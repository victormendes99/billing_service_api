from fastapi import APIRouter
from app.api.v1.endpoints import bills, user


api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["user"])

api_router.include_router(bills.router, prefix="/bills", tags=["bills"])
