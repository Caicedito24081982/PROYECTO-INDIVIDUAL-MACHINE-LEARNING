from fastapi import APIRouter, HTTPException
from app.services.genres import get_user_for_genre

router = APIRouter()

@router.get("/user_for_genre/{genero}")
async def user_for_genre(genero: str):
    try:
        return await get_user_for_genre(genero)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

