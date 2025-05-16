from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

class AccountType(Enum):
    CHECKING = "CHECKING"
    SAVINGS = "SAVINGS"

class AccountStatus(Enum):
    ACTIVE = "active"
    CLOSED = "closed"

class InterestStrategy(Enum):
    SIMPLE = "simple"
    COMPOUND = "compound"

class Account(ABC):
    def __init__(
        self, 
        account_id: str, 
        account_type: AccountType,
        balance: float = 0.0,
        interest_strategy: InterestStrategy = InterestStrategy.SIMPLE,
        last_interest_date: datetime = datetime.now(),
        daily_limit: float = 1000.0,
        monthly_limit: float = 5000.0
    ):
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance
        self.interest_strategy = interest_strategy
        self.daily_limit = daily_limit
        self.monthly_limit = monthly_limit
        self.daily_used = 0.0
        self.monthly_used = 0.0
        self.last_interest_date = datetime.now()

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float):
        pass

class SavingsAccount(Account):
    MIN_BALANCE = 100.0
    
    def withdraw(self, amount: float):
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(f"Withdrawal would go below minimum balance of {self.MIN_BALANCE}")
        self.balance -= amount

class CheckingAccount(Account):
    OVERDRAFT_LIMIT = 500.0
    
    def withdraw(self, amount: float):
        if self.balance - amount < -self.OVERDRAFT_LIMIT:
            raise ValueError("Exceeds overdraft limit")
        self.balance -= amount