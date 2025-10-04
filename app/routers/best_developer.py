from fastapi import APIRouter, HTTPException
from app.services.best_developer import get_best_developer_year
from typing import List, Dict

router = APIRouter()

@router.get("/best_developer_year/{year}")
async def best_developer_year(year: int) -> List[Dict[str, str]]:
    try:
        result = await get_best_developer_year(year)
        if not result:
            raise HTTPException(status_code=404, detail=f"No se encontraron juegos recomendados en el año {year}")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
