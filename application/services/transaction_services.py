from uuid import uuid4
from domain.entities.transaction import Transaction, TransactionType

class TransactionService:
    def __init__(self, account_repo, transaction_repo, limit_service):
        self.account_repo = account_repo
        self.transaction_repo = transaction_repo
        self.limit_service = limit_service

    def deposit(self, account_id: str, amount: float) -> Transaction:
        account = self.account_repo.get_account_by_id(account_id)
        if not account:
            raise ValueError(f"Account {account_id} not found")
        
        account.deposit(amount)
        self.account_repo.update_account(account)
        return self._create_transaction(account_id, amount, TransactionType.DEPOSIT)

    def withdraw(self, account_id: str, amount: float) -> Transaction:
        account = self.account_repo.get_account_by_id(account_id)
        if not account:
            raise ValueError(f"Account {account_id} not found")
        
        self.limit_service.check_daily_limit(account, amount)
        self.limit_service.check_monthly_limit(account, amount)
        
        account.withdraw(amount)
        account.daily_used += amount
        account.monthly_used += amount
        
        self.account_repo.update_account(account)
        return self._create_transaction(account_id, amount, TransactionType.WITHDRAW)

    def _create_transaction(self, account_id: str, amount: float, txn_type: TransactionType) -> Transaction:
        transaction = Transaction(
            transaction_id=str(uuid4()),
            amount=amount,
            transaction_type=txn_type,
            account_id=account_id
        )
        return self.transaction_repo.save_transaction(transaction)