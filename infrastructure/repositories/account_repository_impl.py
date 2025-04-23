from application.interfaces.account_repository import AccountRepository
from domain.entities.account import Account

# infrastructure/repositories/account_repository_impl.py
from application.interfaces.account_repository import AccountRepository
from domain.entities.account import Account  # Only import Account

class InMemoryAccountRepository(AccountRepository):
    def __init__(self):
        self.accounts = {}

    def create_account(self, account: Account) -> str:
        self.accounts[account.account_id] = account
        return account.account_id

    def get_account_by_id(self, account_id: str) -> Account:
        return self.accounts.get(account_id)

    def update_account(self, account: Account) -> None:
        self.accounts[account.account_id] = account