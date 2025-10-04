from fastapi import APIRouter, HTTPException
from app.services.recommendations import get_game_recommendation

router = APIRouter()

@router.get("/recomendacion_juego/{product_id}")
async def recomendacion_juego(product_id: int):
    try:
        return await get_game_recommendation(product_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

