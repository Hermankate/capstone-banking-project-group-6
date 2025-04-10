from uuid import uuid4
from domain.entities.account import Account, SavingsAccount, CheckingAccount, AccountType

class AccountCreationService:
    def __init__(self, account_repository):
        self.account_repo = account_repository
        self.min_savings_deposit = 100.0

    def create_account(self, account_type: AccountType, initial_deposit: float = 0.0) -> str:
        if account_type == AccountType.SAVINGS and initial_deposit < self.min_savings_deposit:
            raise ValueError(f"Minimum initial deposit for savings is {self.min_savings_deposit}")
            
        account_id = str(uuid4())
        account = (
            SavingsAccount(account_id, account_type, initial_deposit)
            if account_type == AccountType.SAVINGS
            else CheckingAccount(account_id, account_type, initial_deposit)
        )
        return self.account_repo.create_account(account)