# presentation/api/routes/transfers.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from application.services.fund_transfer_service import FundTransferService

router = APIRouter(prefix="/transfers")

class TransferRequest(BaseModel):
    source_account_id: str
    destination_account_id: str
    amount: float

@router.post("/")
def transfer_funds(
    request: TransferRequest,
    service: FundTransferService = Depends(get_transfer_service)
):
    try:
        transaction_id = service.transfer_funds(
            request.source_account_id,
            request.destination_account_id,
            request.amount
        )
        return {"transaction_id": transaction_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))