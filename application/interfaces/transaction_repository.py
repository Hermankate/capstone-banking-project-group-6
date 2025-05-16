from abc import ABC, abstractmethod
from domain.entities.transaction import Transaction

class TransactionRepository(ABC):
    @abstractmethod
    def save_transaction(self, transaction: Transaction) -> Transaction:  # ✅ Return Transaction, not str
        pass
    
    @abstractmethod
    def get_transactions_for_account(self, account_id: str) -> list[Transaction]:
        pass