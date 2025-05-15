from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from domain.entities.account import SavingsAccount, CheckingAccount, AccountType  # Import AccountType
from application.services.account_creation_services import AccountCreationService
from infrastructure.repositories.account_repository_impl import InMemoryAccountRepository

router = APIRouter(prefix="/accounts")

# Add dependency function HERE
def get_account_creation_service():
    account_repo = InMemoryAccountRepository()
    return AccountCreationService(account_repo)

class CreateAccountRequest(BaseModel):
    account_type: str  # "SAVINGS" or "CHECKING"
    initial_deposit: float = 0.0

class AccountResponse(BaseModel):
    account_id: str
    account_type: str
    balance: float

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_account(
    request: CreateAccountRequest,
    service: AccountCreationService = Depends(get_account_creation_service)
):
    try:
        # Validate account type
        if request.account_type not in [AccountType.SAVINGS, AccountType.CHECKING]:
            raise ValueError(f"Unsupported account type: {request.account_type}")

        # Create the account
        account_id = service.create_account(request.account_type, request.initial_deposit)
        return {"account_id": account_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


