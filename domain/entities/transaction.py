# domain/entities/transaction.py
from enum import Enum
from datetime import datetime

class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    TRANSFER = "TRANSFER"  # New type

class Transaction:
    def __init__(
        self, 
        transaction_id: str, 
        source_account_id: str,  # Added for transfers
        amount: float, 
        transaction_type: TransactionType,
        destination_account_id: str = None  # Only for TRANSFER
    ):
        self.transaction_id = transaction_id
        self.source_account_id = source_account_id
        self.amount = amount
        self.type = transaction_type
        self.destination_account_id = destination_account_id
        self.timestamp = datetime.now()