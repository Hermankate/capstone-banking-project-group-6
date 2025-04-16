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
from application.services.fund_transfer_service import FundTransferService
from application.services.notification_service import NotificationService, EmailNotification, SMSNotification

# Add to startup
transfer_service = FundTransferService(account_repo, transaction_repo)
notification_service = NotificationService()
notification_service.add_observer(EmailNotification())
notification_service.add_observer(SMSNotification())

# Attach notification to transaction completion
def after_transaction(transaction):
    notification_service.notify_all(transaction)

# Decorate TransactionService methods with logging and notifications
transaction_service.deposit = log_transaction(transaction_service.deposit)
transaction_service.withdraw = log_transaction(transaction_service.withdraw)