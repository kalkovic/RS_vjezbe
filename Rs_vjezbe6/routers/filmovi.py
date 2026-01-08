from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json

from models.movie import Movie

router = APIRouter(prefix="/films", tags=["Films"])

with open("movies.json", "r", encoding="utf-8") as f:
    movies_data = json.load(f)

movies = [Movie(**movie) for movie in movies_data]


@router.get("/", response_model=List[Movie])
def get_all_movies(
    min_year: Optional[int] = Query(None, gt=1900),
    max_year: Optional[int] = None,
    min_rating: Optional[float] = Query(None, ge=0, le=10),
    max_rating: Optional[float] = Query(None, ge=0, le=10),
    type: Optional[str] = Query(None, pattern="^(movie|series)$")
):
    result = movies

    if min_year:
        result = [m for m in result if m.Year >= min_year]
    if max_year:
        result = [m for m in result if m.Year <= max_year]
    if min_rating:
        result = [m for m in result if m.imdbRating >= min_rating]
    if max_rating:
        result = [m for m in result if m.imdbRating <= max_rating]
    if type:
        result = [m for m in result if m.type == type]

    return result


@router.get("/id/{imdb_id}", response_model=Movie)
def get_movie_by_id(imdb_id: str):
    for movie in movies:
        if movie.imdbID == imdb_id:
            return movie
    raise HTTPException(status_code=404, detail="Film nije pronađen")


@router.get("/title/{title}", response_model=Movie)
def get_movie_by_title(title: str):
    for movie in movies:
        if movie.Title.lower() == title.lower():
            return movie
    raise HTTPException(status_code=404, detail="Film nije pronađen")
