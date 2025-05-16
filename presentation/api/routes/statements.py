from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import datetime
from application.services.interest_service import InterestService
from application.services.statement_service import StatementService
from fastapi.responses import FileResponse

router = APIRouter(prefix="/accounts/{account_id}")

class InterestResponse(BaseModel):
    interest: float
    new_balance: float

class StatementRequest(BaseModel):
    month: int
    year: int
    format: str

def get_interest_service():
    pass

def get_statement_service():
    pass

@router.post("/interest/calculate", response_model=InterestResponse)
def calculate_interest(
    account_id: str,
    service: InterestService = Depends(get_interest_service)
):
    try:
        interest = service.calculate_interest(account_id)
        account = service.account_repo.get_account_by_id(account_id)
        return {
            "interest": round(interest, 2),
            "new_balance": round(account.balance, 2)
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get("/statement")
def generate_statement(
    account_id: str,
    month: int,
    year: int,
    format: str,
    service: StatementService = Depends(get_statement_service)
):
    try:
        file_path = service.generate_statement(account_id, month, year, format)
        return FileResponse(file_path, media_type="application/octet-stream")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))