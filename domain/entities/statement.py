from datetime import datetime
from typing import List
from domain.entities.transaction import Transaction

class MonthlyStatement:
    def __init__(self, account_id: str, month: int, year: int):
        self.account_id = account_id
        self.month = month
        self.year = year
        self.transactions: List[Transaction] = []
        self.opening_balance = 0.0
        self.closing_balance = 0.0
        self.interest_earned = 0.0