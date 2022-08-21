from pydantic import BaseModel


class Movie(BaseModel):
    adult: bool
    image_links: list
    originalLanguage: str
    originalTitle: str
    overview: str
    popularity: float
    releaseDate: str
    title: str
    video: bool
    voteAverage: float
    voteCount: int
