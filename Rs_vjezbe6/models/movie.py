from pydantic import BaseModel, Field, validator
from typing import List, Optional, Literal


class Actor(BaseModel):
    name: str
    surname: str


class Writer(BaseModel):
    name: str
    surname: str


class Movie(BaseModel):
    imdbID: str
    Title: str
    Year: int
    Rated: str
    Runtime: int
    Genre: str
    Language: str
    Country: str
    Actors: List[Actor]
    Writer: List[Writer]
    Plot: str

    type: Literal["movie", "series"]
    Images: List[str]

    imdbRating: Optional[float] = 0
    imdbVotes: Optional[int] = 0

    @validator("Year")
    def year_validation(cls, v):
        if v <= 1900:
            raise ValueError("Godina mora biti veća od 1900")
        return v

    @validator("Runtime")
    def runtime_validation(cls, v):
        if v <= 0:
            raise ValueError("Trajanje mora biti veće od 0")
        return v

    @validator("imdbRating")
    def rating_validation(cls, v):
        if not (0 <= v <= 10):
            raise ValueError("Ocjena mora biti između 0 i 10")
        return v

    @validator("imdbVotes")
    def votes_validation(cls, v):
        if v < 0:
            raise ValueError("Broj glasova mora biti >= 0")
        return v
