# from fastapi import FastAPI
# from infrastructure.repositories.account_repository_impl import InMemoryAccountRepository
# from infrastructure.repositories.transaction_repository_impl import InMemoryTransactionRepository
# from application.services.account_creation_services import AccountCreationService
# from application.services.transaction_services import TransactionService
# from presentation.api.routes import accounts, transactions  # Critical import

# app = FastAPI()
# @app.get("/")
# def root():
#     return {"message": "Banking API is running!"}


# # Initialize repositories and services
# account_repo = InMemoryAccountRepository()
# transaction_repo = InMemoryTransactionRepository()

# account_creation_service = AccountCreationService(account_repo)
# transaction_service = TransactionService(account_repo, transaction_repo)


# # Include routers from the routes module
# app.include_router(accounts.router)
# app.include_router(transactions.router)

# # Override dependencies at startup
# @app.on_event("startup")
# async def startup_event():
#     app.dependency_overrides.update({
#         accounts.get_account_creation_service: lambda: account_creation_service,
#         transactions.get_transaction_service: lambda: transaction_service
#     })
# presentation/api/main.py
# from application.services.fund_transfer_service import FundTransferService
# from application.services.logging_service import log_transaction
# from application.services.notification_service import NotificationService, EmailNotification, SMSNotification
# from domain.services import transaction_service
# from infrastructure.repositories.account_repository_impl import InMemoryAccountRepository
# from infrastructure.repositories.transaction_repository_impl import InMemoryTransactionRepository

# account_repo = InMemoryAccountRepository()
# transaction_repo = InMemoryTransactionRepository()

# # Add to startup
# transfer_service = FundTransferService(account_repo, transaction_repo)


from fastapi import FastAPI
from infrastructure.repositories.account_repository_impl import InMemoryAccountRepository
from infrastructure.repositories.transaction_repository_impl import InMemoryTransactionRepository
from application.services.account_creation_services import AccountCreationService
from application.services.transaction_services import TransactionService
from application.services.fund_transfer_service import FundTransferService  # ✅ Import new service
from presentation.api.routes import accounts, transactions, transfers  # Import new routes

app = FastAPI()

# Initialize repositories FIRST
account_repo = InMemoryAccountRepository()
transaction_repo = InMemoryTransactionRepository()

# Initialize services AFTER repositories
account_creation_service = AccountCreationService(account_repo)
transaction_service = TransactionService(account_repo, transaction_repo)
transfer_service = FundTransferService(account_repo, transaction_repo)  

# Include routers
app.include_router(accounts.router)
app.include_router(transactions.router)
app.include_router(transfers.router)  # Add transfers routes

# Dependency injection
@app.on_event("startup")
async def startup_event():
    app.dependency_overrides.update({
        accounts.get_account_creation_service: lambda: account_creation_service,
        transactions.get_transaction_service: lambda: transaction_service,
        transfers.get_transfer_service: lambda: transfer_service  # Add transfer service
    })