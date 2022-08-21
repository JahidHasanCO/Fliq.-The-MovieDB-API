from fastapi import FastAPI
from routes.movie import movie

app = FastAPI()
app.include_router(movie)
