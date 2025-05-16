from application.services.transaction_services import TransactionService
from domain.entities.account import AccountType, CheckingAccount
from infrastructure.repositories.account_repository_impl import InMemoryAccountRepository
from infrastructure.repositories.transaction_repository_impl import InMemoryTransactionRepository
from application.services.limit_service import LimitEnforcementService
from domain.entities.transaction import Transaction, TransactionType
import pytest

def setup_service():
    account_repo = InMemoryAccountRepository()
    transaction_repo = InMemoryTransactionRepository()
    limit_service = LimitEnforcementService()
    # Create account and get its ID
    acc = CheckingAccount("acc1", AccountType.CHECKING, 200)
    account_repo.create_account(acc)
    service = TransactionService(account_repo, transaction_repo, limit_service)
    return service, acc.account_id

def test_deposit():
    service, acc_id = setup_service()
    txn = service.deposit(acc_id, 50)
    assert txn.amount == 50

def test_withdraw():
    service, acc_id = setup_service()
    txn = service.withdraw(acc_id, 50)
    assert txn.amount == 50

def test_withdraw_over_limit():
    service, acc_id = setup_service()
    with pytest.raises(ValueError):
        service.withdraw(acc_id, 2000)  # Over daily limit

def test_deposit_transaction():
    account_repo = InMemoryAccountRepository()
    transaction_repo = InMemoryTransactionRepository()
    limit_service = LimitEnforcementService()
    # Create an account
    acc = CheckingAccount("acc2", AccountType.CHECKING, 100.0)
    account_repo.create_account(acc)
    service = TransactionService(account_repo, transaction_repo, limit_service)
    transaction = service.deposit(acc.account_id, 50.0)
    account = account_repo.get_account_by_id(acc.account_id)
    assert account.balance == 150.0
    assert transaction.amount == 50.0

def test_transaction_creation():
    txn = Transaction("txn1", 100.0, TransactionType.DEPOSIT, account_id="acc1")
    assert txn.amount == 100.0
    assert txn.account_id == "acc1"
    assert txn.transaction_type == TransactionType.DEPOSIT