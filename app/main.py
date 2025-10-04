from fastapi import FastAPI
from app.routers import developers, genres, recommendations, best_developer, reviews_analysis, userdata
from app.services.recommendations import load_recommendation_model

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    load_recommendation_model()

# Incluir todos los routers
app.include_router(developers.router)
app.include_router(genres.router)
app.include_router(recommendations.router)
app.include_router(best_developer.router)
app.include_router(reviews_analysis.router)
app.include_router(userdata.router)

