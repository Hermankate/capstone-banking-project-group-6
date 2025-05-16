from fastapi import FastAPI
from datetime import datetime
from infrastructure.repositories.account_repository_impl import InMemoryAccountRepository
from infrastructure.repositories.transaction_repository_impl import InMemoryTransactionRepository
from application.services.account_creation_services import AccountCreationService
from application.services.transaction_services import TransactionService
from application.services.fund_transfer_service import FundTransferService
from application.services.notification_services import NotificationService
from application.services.interest_service import InterestService
from application.services.limit_service import LimitEnforcementService
from application.services.statement_adapter import StatementAdapter
from application.services.statement_service import StatementService
from infrastructure.adapters.notification_adapter import MockNotificationAdapter
#from infrastructure.adapters. import StatementAdapter
from presentation.api.routes import accounts, transactions, transfers, statements

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Banking API is running!"}

# Initialize repositories
account_repo = InMemoryAccountRepository()
transaction_repo = InMemoryTransactionRepository()

# Initialize adapters and services
notification_adapter = MockNotificationAdapter()
statement_adapter = StatementAdapter()
limit_service = LimitEnforcementService()

notification_service = NotificationService(notification_adapter)
interest_service = InterestService(account_repo)
statement_service = StatementService(transaction_repo, statement_adapter)

# Core services initialization
account_creation_service = AccountCreationService(account_repo)
transaction_service = TransactionService(
    account_repo, 
    transaction_repo,
    limit_service
)
fund_transfer_service = FundTransferService(
    account_repo,
    transaction_repo,
    notification_service
)

# Include all routers
app.include_router(accounts.router)
app.include_router(transactions.router)
app.include_router(transfers.router)
app.include_router(statements.router)

# Dependency injection setup
@app.on_event("startup")
async def startup_event():
    app.dependency_overrides.update({
        accounts.get_account_creation_service: lambda: account_creation_service,
        transactions.get_transaction_service: lambda: transaction_service,
        transfers.get_fund_transfer_service: lambda: fund_transfer_service,
        statements.get_statement_service: lambda: statement_service,
        #statements.get_interest_service: lambda: interest_service
    })