from fastapi import APIRouter

from models.movie import Movie
from config.db import db
from schemas.movie import movieEntity, moviesEntity

movie = APIRouter()


@movie.get('/movies')
async def find_all_users():
    return moviesEntity(db.user.find())


@movie.post('/movie')
async def create_user(movie: Movie):
    db.movie.insert_one(dict(movie))
    return moviesEntity(db.user.find())
