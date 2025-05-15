from uuid import uuid4
from domain.entities.transaction import Transaction, TransactionType
# filepath: application/services/transaction_services.py
from application.services.logging_service import log_transaction
from application.services.notification_service import NotificationService

class TransactionService:
    def __init__(self, account_repo, transaction_repo, limit_service, notification_service: NotificationService):
        self.account_repo = account_repo
        self.transaction_repo = transaction_repo
        self.limit_service = limit_service  # Add limit_service
        self.notification_service = notification_service  # Add notification_service

    @log_transaction
    def deposit(self, account_id: str, amount: float) -> Transaction:
        account = self.account_repo.get_account_by_id(account_id)
        if not account:
            raise ValueError(f"Account {account_id} not found")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        account.deposit(amount)
        self.account_repo.update_account(account)
        transaction = self._create_transaction(account_id, amount, TransactionType.DEPOSIT)
        self.notification_service.notify_all(transaction)
        return transaction

    @log_transaction
    def withdraw(self, account_id: str, amount: float) -> Transaction:
        account = self.account_repo.get_account_by_id(account_id)
        if not account:
            raise ValueError(f"Account {account_id} not found")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if not self.limit_service.check_limit(account_id, amount):
            raise ValueError("Transaction exceeds the allowed limit.")
        account.withdraw(amount)
        self.account_repo.update_account(account)
        transaction = self._create_transaction(account_id, amount, TransactionType.WITHDRAW)
        self.notification_service.notify_all(transaction)
        return transaction

    def _create_transaction(
        self, 
        account_id: str, 
        amount: float, 
        txn_type: TransactionType
    ) -> Transaction:
        transaction = Transaction(
            transaction_id=str(uuid4()),
            source_account_id=account_id,  # Use source_account_id
            amount=amount,
            transaction_type=txn_type
        )
        return self.transaction_repo.save_transaction(transaction)  # Returns Transaction object