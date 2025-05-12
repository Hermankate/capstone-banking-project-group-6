from uuid import uuid4
from domain.entities.transaction import Transaction, TransactionType
from domain.services.transaction_service import TransferService

class FundTransferService:
    def __init__(self, account_repo, transaction_repo):
        self.account_repo = account_repo
        self.transaction_repo = transaction_repo

    def transfer_funds(
        self, 
        source_account_id: str, 
        destination_account_id: str, 
        amount: float
    ) -> str:
        # Fetch accounts
        source = self.account_repo.get_account_by_id(source_account_id)
        dest = self.account_repo.get_account_by_id(destination_account_id)
        
        if not source or not dest:
            raise ValueError("Invalid account ID(s)")
        
        try:
            # Perform transfer
            TransferService.transfer(source, dest, amount)
            
            # Update accounts
            self.account_repo.update_account(source)
            self.account_repo.update_account(dest)
            
            # Log transfer transaction
            transaction = self._create_transfer_transaction(
                source_account_id, 
                destination_account_id, 
                amount
            )
            return transaction.transaction_id
        except Exception as e:
            # Rollback logic (if applicable)...
            raise ValueError(f"Transfer failed: {str(e)}")

    def _create_transfer_transaction(self, source_id, dest_id, amount):
        transaction = Transaction(
            transaction_id=str(uuid4()),
            source_account_id=source_id,
            amount=amount,
            transaction_type=TransactionType.TRANSFER,
            destination_account_id=dest_id
        )
        return self.transaction_repo.save_transaction(transaction)