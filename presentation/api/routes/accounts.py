# from fastapi import APIRouter, Depends, HTTPException, status
# from pydantic import BaseModel
# from domain.entities.account import AccountType, CheckingAccount, SavingsAccount
# from application.services.account_creation_services import AccountCreationService
# # router = APIRouter(prefix="/accounts")


from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from domain.entities.account import SavingsAccount, CheckingAccount  # ✅ Remove AccountType
from application.services.account_creation_services import AccountCreationService
from infrastructure.repositories.account_repository_impl import InMemoryAccountRepository
def get_account_creation_service():
    # Initialize the repository
    account_repo = InMemoryAccountRepository()
    # Return the service instance
    return AccountCreationService(account_repo)

router = APIRouter(prefix="/accounts")

class CreateAccountRequest(BaseModel):
    account_type: str  # "SAVINGS" or "CHECKING"
    initial_deposit: float = 0.0

class AccountResponse(BaseModel):
    account_id: str
    account_type: str  # Return string instead of Enum
    balance: float

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AccountResponse)
def create_account(
    request: CreateAccountRequest,
    service: AccountCreationService = Depends(get_account_creation_service)
):
    try:
        # Map the string to the correct account class
        account_class = (
            SavingsAccount if request.account_type == "SAVINGS" 
            else CheckingAccount
        )
        account_id = service.create_account(account_class, request.initial_deposit)
        account = service.account_repo.get_account_by_id(account_id)
        return {
            "account_id": account_id,
            "account_type": account.account_type,  # Use the property
            "balance": account.balance
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))