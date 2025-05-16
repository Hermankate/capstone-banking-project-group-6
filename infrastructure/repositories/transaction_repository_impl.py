from application.interfaces.transaction_repository import TransactionRepository
from domain.entities.transaction import Transaction, TransactionType

class InMemoryTransactionRepository(TransactionRepository):
    def __init__(self):
        self.transactions = {}

    def save_transaction(self, transaction: Transaction) -> Transaction:
        self.transactions[transaction.transaction_id] = transaction
        return transaction

    def get_transactions_for_account(self, account_id: str) -> list[Transaction]:
        return [txn for txn in self.transactions.values() if 
                (txn.transaction_type != TransactionType.TRANSFER and txn.account_id == account_id) or
                (txn.transaction_type == TransactionType.TRANSFER and 
                 (txn.source_account_id == account_id or txn.destination_account_id == account_id))]