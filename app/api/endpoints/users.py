# app/api/endpoints/users.py 

from fastapi import APIRouter, Depends
from app.db.repositories.users import UserRepository
from app.models.users import UserCreate, UserUpdate

router = APIRouter()

@router.get("/")
async def get_all_users(users: UserRepository = Depends()):
    return await users.get_all()
    
@router.post("/")
async def create_user(user: UserCreate, users: UserRepository = Depends()):
    return await users.create(user)

@router.put("/{user_id}")
async def update_user(user_id: int, user: UserUpdate, users: UserRepository = Depends()):
    return await users.update(user_id, user)