from fastapi import FastAPI
from app.routers import developers, genres, recommendations
from app.services.recommendations import load_recommendation_model

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    load_recommendation_model()

app.include_router(developers.router)
app.include_router(genres.router)
app.include_router(recommendations.router)

