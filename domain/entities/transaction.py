from datetime import datetime
from enum import Enum
from typing import Optional

class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    TRANSFER = "TRANSFER"

class Transaction:
    def __init__(
        self,
        transaction_id: str,
        amount: float,
        transaction_type: TransactionType,
        account_id: Optional[str] = None,
        source_account_id: Optional[str] = None,
        destination_account_id: Optional[str] = None
    ):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()
        
        if transaction_type == TransactionType.TRANSFER:
            if not source_account_id or not destination_account_id:
                raise ValueError("Transfer requires source and destination account IDs")
            self.source_account_id = source_account_id
            self.destination_account_id = destination_account_id
        else:
            if not account_id:
                raise ValueError("Account ID required for non-transfer transactions")
            self.account_id = account_id