from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from application.services.limit_service import LimitService

router = APIRouter(prefix="/limits")

class LimitRequest(BaseModel):
    account_id: str
    limit_type: str  # "DAILY" or "MONTHLY"
    max_amount: float

@router.post("/set")
def set_limit(
    request: LimitRequest,
    service: LimitService = Depends(get_limit_service)
):
    try:
        service.set_limit(request.account_id, request.limit_type, request.max_amount)
        return {"message": "Limit updated successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))