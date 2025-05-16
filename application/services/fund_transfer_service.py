from uuid import uuid4
from domain.entities.transaction import Transaction, TransactionType

class FundTransferService:
    def __init__(self, account_repo, transaction_repo, notification_service=None, logging_service=None):
        self.account_repo = account_repo
        self.transaction_repo = transaction_repo
        self.notification_service = notification_service
        self.logging_service = logging_service

    def transfer_funds(self, source_id: str, dest_id: str, amount: float) -> Transaction:
        # Get accounts
        source = self.account_repo.get_account_by_id(source_id)
        dest = self.account_repo.get_account_by_id(dest_id)
        if not source or not dest:
            raise ValueError("Source or destination account not found")

        # Withdraw and deposit
        source.withdraw(amount)
        dest.deposit(amount)

        # Update accounts
        self.account_repo.update_account(source)
        self.account_repo.update_account(dest)

        # Create transaction record
        # When creating transfer transactions
        txn = Transaction(
            transaction_id=str(uuid4()),
            amount=amount,
            transaction_type=TransactionType.TRANSFER,  # Use renamed attribute
            source_account_id=source_id,
            destination_account_id=dest_id
        )
        saved_txn = self.transaction_repo.save_transaction(txn)

        # Trigger notifications and logging
        if self.notification_service:
            self.notification_service.notify(saved_txn)
        if self.logging_service:
            self.logging_service.log_transaction(saved_txn)
            
        return saved_txn