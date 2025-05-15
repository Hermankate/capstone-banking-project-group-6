from domain.entities.account import Account, AccountType, SavingsAccount, CheckingAccount
from application.interfaces.account_repository import AccountRepository

class AccountCreationService:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def create_account(self, account_type: str, initial_deposit: float = 0.0) -> str:
        # Validate initial deposit
        if account_type == AccountType.SAVINGS and initial_deposit < 100:
            raise ValueError("Minimum savings deposit is $100")

        # Instantiate the appropriate account type
        if account_type == AccountType.SAVINGS:
            account = SavingsAccount(account_id=None, balance=initial_deposit)
        elif account_type == AccountType.CHECKING:
            account = CheckingAccount(account_id=None, balance=initial_deposit)
        else:
            raise ValueError(f"Unsupported account type: {account_type}")

        # Save the account and return the account ID
        return self.account_repository.create_account(account)


from domain.entities.account import SavingsAccount, CheckingAccount

class AccountFactory:
    @staticmethod
    def create_account(account_type: str, account_id: str, initial_deposit: float):
        if account_type == "SAVINGS":
            return SavingsAccount(account_id, initial_deposit)
        elif account_type == "CHECKING":
            return CheckingAccount(account_id, initial_deposit)
        else:
            raise ValueError(f"Unsupported account type: {account_type}")