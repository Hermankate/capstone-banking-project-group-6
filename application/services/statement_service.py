from datetime import datetime
from domain.entities.statement import MonthlyStatement
from domain.entities.transaction import Transaction

class StatementService:
    def __init__(self, transaction_repo, account_repo):
        self.transaction_repo = transaction_repo
        self.account_repo = account_repo

    def generate_statement(self, account_id: str, month: int, year: int) -> MonthlyStatement:
        statement = MonthlyStatement(account_id, month, year)
        transactions = self.transaction_repo.get_transactions_for_account(account_id)
        statement.transactions = [
            txn for txn in transactions if txn.timestamp.month == month and txn.timestamp.year == year
        ]
        statement.opening_balance = self.account_repo.get_account_by_id(account_id).balance
        statement.closing_balance = statement.opening_balance + sum(txn.amount for txn in statement.transactions)
        return statement