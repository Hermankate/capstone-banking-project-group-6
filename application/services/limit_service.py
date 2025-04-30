from domain.entities.limit import TransactionLimit

class LimitService:
    def __init__(self, account_repo):
        self.account_repo = account_repo

    def check_limit(self, account_id: str, amount: float) -> bool:
        account = self.account_repo.get_account_by_id(account_id)
        if account.limit.needs_reset():
            account.limit.reset()
        return account.limit.is_exceeded(account.current_usage + amount)