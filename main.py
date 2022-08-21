from fastapi import FastAPI

from routes.movie import appMovieRouter

app = FastAPI()
app.include_router(appMovieRouter)

