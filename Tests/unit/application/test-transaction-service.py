from application.services.transaction_services import TransactionService
from domain.entities.account import AccountType, CheckingAccount
from infrastructure.repositories.account_repository_impl import InMemoryAccountRepository
from infrastructure.repositories.transaction_repository_impl import InMemoryTransactionRepository

def test_deposit_transaction():
    account_repo = InMemoryAccountRepository()
    transaction_repo = InMemoryTransactionRepository()
    
    # Create an account
    account_repo.create_account(CheckingAccount("acc1", AccountType.CHECKING, 100.0))
    
    service = TransactionService(account_repo, transaction_repo)
    transaction = service.deposit("acc1", 50.0)
    
    account = account_repo.get_account_by_id("acc1")
    assert account.balance == 150.0
    assert transaction.amount == 50.0