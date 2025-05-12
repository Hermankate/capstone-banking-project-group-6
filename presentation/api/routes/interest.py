from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import datetime
from application.services.interest_service import InterestService, get_interest_service

router = APIRouter(prefix="/interest")

class InterestRequest(BaseModel):
    account_id: str
    start_date: datetime
    end_date: datetime

@router.post("/calculate")
def calculate_interest(
    request: InterestRequest,
    service: InterestService = Depends(get_interest_service)
):
    try:
        interest = service.calculate_interest(request.account_id, request.start_date, request.end_date)
        return {"interest_earned": interest}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))