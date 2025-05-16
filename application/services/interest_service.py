from datetime import datetime
from domain.entities.account import InterestStrategy

class InterestService:
    def __init__(self, account_repo):
        self.account_repo = account_repo

    def calculate_interest(self, account_id: str) -> float:
        account = self.account_repo.get_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")
            
        days = (datetime.now() - account.last_interest_date).days
        if days <= 0:
            return 0.0  # No interest if called same day

        if account.interest_strategy == InterestStrategy.SIMPLE:
            interest = account.balance * 0.02 * days / 365
        else:
            interest = account.balance * ((1.02 ** (days/365)) - 1)
        
        account.balance += interest
        account.last_interest_date = datetime.now()
        self.account_repo.update_account(account)
        return interest