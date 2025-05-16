from domain.entities.transaction import TransactionType

class NotificationService:
    def __init__(self, adapter):
        self.adapter = adapter

    def notify(self, transaction):
        if transaction.transaction_type == TransactionType.TRANSFER:
            msg = f"Transferred ${transaction.amount} from {transaction.source_account_id} to {transaction.destination_account_id}"
        else:
            msg = f"{transaction.transaction_type.value} of ${transaction.amount} on account {transaction.account_id}"
        self.adapter.send("user@example.com", msg)