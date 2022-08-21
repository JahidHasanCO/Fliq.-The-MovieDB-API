from fastapi import APIRouter

from models.movie import Movie
from config.db import db
from schemas.movie import serializeDict , serializeList
from bson import ObjectId

appMovieRouter = APIRouter()


@appMovieRouter.get('/movie')
async def movies():
    return serializeList(db.movies.find())

@appMovieRouter.get('/movies/{id}')
async def movie_details(id):
    return serializeDict(db.movies.find_one({"_id":ObjectId(id)}))

@appMovieRouter.post('/movie')
async def movie(movie: Movie):
    db.movies.insert_one(dict(movie))
    return {
        "msg": "Successfully movie added.",
        "Status Code": 200
    }


@appMovieRouter.put('/movie/{id}')
async def update_movie(id,movie: Movie):
    db.movies.find_one_and_update({"_id":ObjectId(id)},
        {"$set": dict(movie)}
    )
    return {
        "msg": "Successfully movie Updated.",
    }


@appMovieRouter.delete('/movie/{id}')
async def delete_movie(id):
    db.movies.find_one_and_delete({"_id":ObjectId(id)})
    return {
        "msg": "Successfully Deleted.",
    }
