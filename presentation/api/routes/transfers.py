from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from application.services.fund_transfer_service import FundTransferService

router = APIRouter(prefix="/accounts")

class TransferRequest(BaseModel):
    source_account_id: str
    destination_account_id: str
    amount: float

class TransferResponse(BaseModel):
    transaction_id: str
    amount: float
    type: str
    source: str
    destination: str
    timestamp: str

def get_fund_transfer_service():
    pass  # Overridden in main

@router.post("/transfer", response_model=TransferResponse)
def transfer_funds(
    request: TransferRequest,
    service: FundTransferService = Depends(get_fund_transfer_service)
):
    try:
        txn = service.transfer_funds(request.source_account_id, request.destination_account_id, request.amount)
        return {
            "transaction_id": txn.transaction_id,
            "amount": txn.amount,
            "type": txn.transaction_type.value,
            "source": txn.source_account_id,
            "destination": txn.destination_account_id,
            "timestamp": txn.timestamp.isoformat()
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))