
from uuid import uuid4
from domain.entities.account import Account, SavingsAccount, CheckingAccount

class AccountCreationService:
    def __init__(self, account_repository):
        self.account_repo = account_repository
        self.min_savings_deposit = 100.0

    def create_account(
        self, 
        account_class: type[Account],  # SavingsAccount or CheckingAccount
        initial_deposit: float = 0.0
    ) -> str:
        if account_class == SavingsAccount and initial_deposit < self.min_savings_deposit:
            raise ValueError(f"Minimum initial deposit for savings is {self.min_savings_deposit}")
            
        account_id = str(uuid4())
        account = account_class(account_id=account_id, balance=initial_deposit)
        return self.account_repo.create_account(account)