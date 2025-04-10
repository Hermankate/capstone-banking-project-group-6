from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from domain.entities.account import AccountType
from application.services.account_creation_services import AccountCreationService
router = APIRouter(prefix="/accounts")

class CreateAccountRequest(BaseModel):
    account_type: AccountType
    initial_deposit: float = 0.0

class AccountResponse(BaseModel):
    account_id: str
    account_type: AccountType
    balance: float

def get_account_creation_service():
    pass  # Implementation provided in main.py

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AccountResponse)
def create_account(
    request: CreateAccountRequest,
    service: AccountCreationService = Depends(get_account_creation_service)
):
    try:
        account_id = service.create_account(request.account_type, request.initial_deposit)
        account = service.account_repo.get_account_by_id(account_id)
        return {
            "account_id": account_id,
            "account_type": account.account_type,
            "balance": account.balance
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))