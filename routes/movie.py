from fastapi import APIRouter

from models.movie import Movie
from config.db import db
from schemas.movie import movieEntity, moviesEntity

appMovieRouter = APIRouter()


@appMovieRouter.get('/movies')
async def movies():
    return moviesEntity(db.movies.find())


@appMovieRouter.post('/movie')
async def movie(movie: Movie):
    db.movies.insert_one(dict(movie))
    return {
        "msg": "Successfully movie added.",
        "Status Code": 201
    }
