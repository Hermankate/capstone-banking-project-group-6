from application.interfaces.transaction_repository import TransactionRepository
from domain.entities.transaction import Transaction

class InMemoryTransactionRepository(TransactionRepository):
    def __init__(self):
        self.transactions = {}

    def save_transaction(self, transaction: Transaction) -> Transaction:  # ✅ Correct return type
        self.transactions[transaction.transaction_id] = transaction
        return transaction  # Return the object, not the ID

    def get_transactions_for_account(self, account_id: str) -> list[Transaction]:
        return [txn for txn in self.transactions.values() if txn.account_id == account_id]