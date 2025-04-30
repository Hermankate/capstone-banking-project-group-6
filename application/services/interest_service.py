from datetime import datetime
from domain.entities.account import Account
from domain.entities.interest_strategy import InterestStrategy

class InterestService:
    def __init__(self, interest_strategy: InterestStrategy):
        self.interest_strategy = interest_strategy

    def calculate_interest(self, account: Account, start_date: datetime, end_date: datetime) -> float:
        days = (end_date - start_date).days
        return self.interest_strategy.calculate_interest(account.balance, days)