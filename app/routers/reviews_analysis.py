from fastapi import APIRouter, HTTPException
from app.services.reviews_analysis import get_developer_reviews_analysis
from typing import Dict

router = APIRouter()

@router.get("/developer_reviews_analysis/{desarrolladora}")
async def developer_reviews_analysis(desarrolladora: str) -> Dict[str, Dict[str, int]]:
    try:
        return await get_developer_reviews_analysis(desarrolladora)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
