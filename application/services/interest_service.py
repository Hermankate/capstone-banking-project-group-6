from datetime import datetime
from domain.entities.account import Account
from domain.entities.interest_strategy import InterestStrategy

class InterestService:
    def __init__(self, interest_strategy: InterestStrategy, account_repo):
        self.interest_strategy = interest_strategy
        self.account_repo = account_repo

    def calculate_interest(self, account: Account, start_date: datetime, end_date: datetime) -> float:
        days = (end_date - start_date).days
        return self.interest_strategy.calculate_interest(account.balance, days)

    def apply_interest_to_account(self, account_id: str):
        account = self.account_repo.get_account_by_id(account_id)
        if not account.interest_strategy:
            raise ValueError("No interest strategy assigned to this account.")
        interest = account.interest_strategy.calculate_interest(account.balance, 30)  # Assume 30 days
        account.deposit(interest)
        self.account_repo.update_account(account)