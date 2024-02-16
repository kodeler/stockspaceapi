# app/models/users.py

from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str
    
class UserCreate(UserBase):
    password: str
    
class UserUpdate(UserBase):
    password: Optional[str] = None