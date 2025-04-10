from fastapi import FastAPI
from infrastructure.repositories.account_repository_impl import InMemoryAccountRepository
from infrastructure.repositories.transaction_repository_impl import InMemoryTransactionRepository
from application.services.account_creation_services import AccountCreationService
from application.services.transaction_services import TransactionService
from presentation.api.routes import accounts, transactions  # Critical import

app = FastAPI()
@app.get("/")
def root():
    return {"message": "Banking API is running!"}


# Initialize repositories and services
account_repo = InMemoryAccountRepository()
transaction_repo = InMemoryTransactionRepository()

account_creation_service = AccountCreationService(account_repo)
transaction_service = TransactionService(account_repo, transaction_repo)


# Include routers from the routes module
app.include_router(accounts.router)
app.include_router(transactions.router)

# Override dependencies at startup
@app.on_event("startup")
async def startup_event():
    app.dependency_overrides.update({
        accounts.get_account_creation_service: lambda: account_creation_service,
        transactions.get_transaction_service: lambda: transaction_service
    })