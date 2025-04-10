from datetime import datetime
from enum import Enum

class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"

class Transaction:
    def __init__(
        self, 
        transaction_id: str, 
        account_id: str, 
        amount: float, 
        transaction_type: TransactionType  # ✅ Correct attribute name
    ):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        self.type = transaction_type  # ✅ Maps to TransactionType enum
        self.timestamp = datetime.now()