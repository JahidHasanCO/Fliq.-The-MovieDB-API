from fastapi import APIRouter

from models.user import User
from config.db import db
from schemas.user import userEntity, usersEntity

user = APIRouter()


@user.get('/')
async def find_all_users():
    return usersEntity(db.user.find())


@user.post('/')
async def create_user(user: User):
    db.user.insert_one(dict(user))
    return usersEntity(db.user.find())
