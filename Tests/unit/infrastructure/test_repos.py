from infrastructure.repositories.account_repository_impl import InMemoryAccountRepository
from domain.entities.account import SavingsAccount, AccountType
from infrastructure.repositories.transaction_repository_impl import InMemoryTransactionRepository
from domain.entities.transaction import Transaction, TransactionType

def test_save_and_get_account():
    repo = InMemoryAccountRepository()
    acc = SavingsAccount("id1", AccountType.SAVINGS, balance=100)
    repo.create_account(acc)
    fetched = repo.get_account_by_id("id1")
    assert fetched.account_id == "id1"
    assert fetched.balance == 100

def test_update_account():
    repo = InMemoryAccountRepository()
    acc = SavingsAccount("id2", AccountType.SAVINGS, balance=100)
    repo.create_account(acc)
    acc.deposit(50)
    repo.update_account(acc)
    fetched = repo.get_account_by_id("id2")
    assert fetched.balance == 150

def test_save_and_get_transaction():
    repo = InMemoryTransactionRepository()
    txn = Transaction("txn1", 100, TransactionType.DEPOSIT, account_id="acc1")
    repo.save_transaction(txn)
    txns = repo.get_transactions_for_account("acc1")
    assert len(txns) == 1
    assert txns[0].transaction_id == "txn1"