# app/api/api_router.py

from fastapi import APIRouter

from app.api.endpoints import users, items, orders
 
router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(items.router, prefix="/items", tags=["items"]) 
router.include_router(orders.router, prefix="/orders", tags=["orders"])
