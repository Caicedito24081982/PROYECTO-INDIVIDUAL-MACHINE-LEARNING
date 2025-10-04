from fastapi import APIRouter, Depends, HTTPException
from app.services.developers import get_developer_stats

router = APIRouter()

@router.get("/developer/{desarrollador}")
async def developer_info(desarrollador: str):
    try:
        return await get_developer_stats(desarrollador)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

