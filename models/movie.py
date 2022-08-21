from pydantic import BaseModel


class Movie(BaseModel):
    name: str
    email: str
    password: str
