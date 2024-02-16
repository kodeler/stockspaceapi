# app/db/repositories/users.py

from app.db.database import async_session
from app.models.users import UserCreate, UserUpdate

class UserRepository:
    def __init__(self, session=async_session):
        self.session = session

    async def get_all(self):
        # query db
        pass

    async def create(self, user: UserCreate):
        # create user in db
        pass

    async def update(self, user_id: int, user: UserUpdate):
        # update user in db
        pass
        