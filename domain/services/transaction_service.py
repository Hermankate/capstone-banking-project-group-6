# domain/services/transfer_service.py
from domain.entities.account import Account
from domain.entities.transaction import TransactionType

class TransferService:
    @staticmethod
    def transfer(
        source_account: Account, 
        destination_account: Account, 
        amount: float
    ) -> None:
        # Withdraw from source
        source_account.withdraw(amount)
        # Deposit into destination
        destination_account.deposit(amount)