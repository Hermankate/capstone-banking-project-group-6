from abc import ABC, abstractmethod
from datetime import datetime
from domain.entities.limit import TransactionLimit, LimitType

class AccountType:
    SAVINGS = "SAVINGS"
    CHECKING = "CHECKING"

class AccountStatus:
    ACTIVE = "active"
    CLOSED = "closed"

class Account(ABC):
    def __init__(
        self, 
        account_id: str, 
        balance: float = 0.0, 
        status: str = AccountStatus.ACTIVE, 
        account_type: str = None
    ):
        self.account_id = account_id
        self.balance = balance
        self.status = status
        self.account_type = account_type
        self.creation_date = datetime.now()
        self.interest_strategy = None
        self.limit = TransactionLimit(LimitType.DAILY, max_amount=1000.0)  # Default limit

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float):
        pass


class SavingsAccount(Account):
    MIN_BALANCE = 100.0

    def __init__(self, account_id: str, balance: float = 0.0, status: str = AccountStatus.ACTIVE):
        super().__init__(account_id, balance, status, account_type=AccountType.SAVINGS)

    def withdraw(self, amount: float):
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(f"Withdrawal would go below minimum balance of {self.MIN_BALANCE}")
        self.balance -= amount


class CheckingAccount(Account):
    OVERDRAFT_LIMIT = 500.0

    def __init__(self, account_id: str, balance: float = 0.0, status: str = AccountStatus.ACTIVE):
        super().__init__(account_id, balance, status, account_type=AccountType.CHECKING)

    def withdraw(self, amount: float):
        if self.balance - amount < -self.OVERDRAFT_LIMIT:
            raise ValueError("Exceeds overdraft limit")
        self.balance -= amount

initial_deposit = 0.0  # Define a default initial deposit value
account_type = AccountType.SAVINGS  # Define a valid account type

# Example instantiation logic
if account_type == AccountType.SAVINGS:
    account = SavingsAccount(
        account_id="12345",  # Replace with actual account ID logic
        balance=initial_deposit,
        status="ACTIVE"
    )
elif account_type == AccountType.CHECKING:
    account = CheckingAccount(
        account_id="12345",  # Replace with actual account ID logic
        balance=initial_deposit,
        status="ACTIVE"
    )
else:
    raise ValueError(f"Unsupported account type: {account_type}")