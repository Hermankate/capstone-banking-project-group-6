from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from application.services.transaction_services import TransactionService
router = APIRouter(prefix="/accounts/{account_id}")

class TransactionRequest(BaseModel):
    amount: float

class TransactionResponse(BaseModel):
    transaction_id: str
    amount: float
    type: str
    timestamp: str

def get_transaction_service():
    pass  # Implementation provided in main.py

@router.post("/deposit", response_model=TransactionResponse)
def deposit(
    account_id: str,
    request: TransactionRequest,
    service: TransactionService = Depends(get_transaction_service)
):
    try:
        transaction = service.deposit(account_id, request.amount)
        return {
            "transaction_id": transaction.transaction_id,
            "amount": transaction.amount,
            "type": transaction.type.value,
            "timestamp": transaction.timestamp.isoformat()
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/withdraw", response_model=TransactionResponse)
def withdraw(
    account_id: str,
    request: TransactionRequest,
    service: TransactionService = Depends(get_transaction_service)
):
    try:
        transaction = service.withdraw(account_id, request.amount)
        return {
            "transaction_id": transaction.transaction_id,
            "amount": transaction.amount,
            "type": transaction.type.value,
            "timestamp": transaction.timestamp.isoformat()
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

class BalanceResponse(BaseModel):
    balance: float
    available_balance: float  # Add logic for available balance if needed

@router.get("/balance", response_model=BalanceResponse)
def get_balance(
    account_id: str,
    service: TransactionService = Depends(get_transaction_service)
):
    account = service.account_repo.get_account_by_id(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"balance": account.balance, "available_balance": account.balance}

@router.get("/transactions", response_model=list[TransactionResponse])
def get_transactions(
    account_id: str,
    service: TransactionService = Depends(get_transaction_service)
):
    transactions = service.transaction_repo.get_transactions_for_account(account_id)
    return [
        {
            "transaction_id": txn.transaction_id,
            "amount": txn.amount,
            "type": txn.type.value,
            "timestamp": txn.timestamp.isoformat()
        } for txn in transactions
    ]