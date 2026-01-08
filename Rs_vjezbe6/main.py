from fastapi import FastAPI
from routers.filmovi import router as filmovi_router

app = FastAPI(title="Movies API")

app.include_router(filmovi_router)
