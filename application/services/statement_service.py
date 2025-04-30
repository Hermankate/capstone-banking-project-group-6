from datetime import datetime
from domain.entities.statement import MonthlyStatement
from domain.entities.transaction import Transaction

class StatementService:
    def __init__(self, transaction_repo):
        self.transaction_repo = transaction_repo

    def generate_statement(self, account_id: str, month: int, year: int) -> MonthlyStatement:
        statement = MonthlyStatement(account_id, month, year)
        transactions = self.transaction_repo.get_transactions_for_account(account_id)
        
        # Filter transactions by month/year
        statement.transactions = [
            txn for txn in transactions
            if txn.timestamp.month == month and txn.timestamp.year == year
        ]
        
        # Calculate opening/closing balance and interest
        # (Assume these are fetched from the account)
        return statement