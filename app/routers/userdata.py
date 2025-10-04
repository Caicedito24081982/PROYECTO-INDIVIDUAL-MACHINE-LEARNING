from fastapi import APIRouter, HTTPException
from app.services.userdata import get_userdata
from typing import Dict

router = APIRouter()

@router.get("/userdata/{User_id}")
async def userdata(User_id: str) -> Dict[str, str]:
    try:
        return await get_userdata(User_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
