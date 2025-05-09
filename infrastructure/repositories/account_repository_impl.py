from typing import Dict, Optional
from domain.entities.account import Account
from application.interfaces.account_repository import AccountRepository

class InMemoryAccountRepository(AccountRepository):
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
        self.next_id = 1  # Simple ID generator

    def create_account(self, account: Account) -> str:
        account.account_id = str(self.next_id)
        self.accounts[account.account_id] = account
        self.next_id += 1
        return account.account_id

    def get_account_by_id(self, account_id: str) -> Optional[Account]:
        return self.accounts.get(account_id)

    def update_account(self, account: Account) -> None:
        if account.account_id in self.accounts:
            self.accounts[account.account_id] = account










# # infrastructure/repositories/account_repository_impl.py
# from application.interfaces.account_repository import AccountRepository
# from domain.entities.account import Account  # Only import Account

# class InMemoryAccountRepository(AccountRepository):
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self, account: Account) -> str:
#         self.accounts[account.account_id] = account
#         return account.account_id
