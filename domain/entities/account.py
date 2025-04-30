# from abc import ABC, abstractmethod
# from datetime import datetime
# from enum import Enum

# class AccountType(Enum):
#     CHECKING = "CHECKING"
#     SAVINGS = "SAVINGS"

# class AccountStatus(Enum):
#     ACTIVE = "active"
#     CLOSED = "closed"

# class Account(ABC):
#     def __init__(self, account_id: str, account_type: AccountType, 
#                  balance: float = 0.0, status: AccountStatus = AccountStatus.ACTIVE):
#         self.account_id = account_id
#         self.account_type = account_type
#         self.balance = balance
#         self.status = status
#         self.creation_date = datetime.now()

#     def deposit(self, amount: float):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self.balance += amount

#     @abstractmethod
#     def withdraw(self, amount: float):
#         pass


from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

class AccountStatus(Enum):
    ACTIVE = "active"
    CLOSED = "closed"

class Account(ABC):
    def __init__(
        self, 
        account_id: str, 
        balance: float = 0.0, 
        status: AccountStatus = AccountStatus.ACTIVE
    ):
        self.account_id = account_id
        self.balance = balance
        self.status = status
        self.creation_date = datetime.now()

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    # Add abstract property to enforce account_type in subclasses
    @property
    @abstractmethod
    def account_type(self) -> str:
        pass


class SavingsAccount(Account):
        MIN_BALANCE = 100.0

        @property
        def account_type(self) -> str:
            return "SAVINGS"  # Directly return the type as a string
        
        def withdraw(self, amount: float):
            if self.balance - amount < self.MIN_BALANCE:
                raise ValueError(f"Withdrawal would go below minimum balance of {self.MIN_BALANCE}")
            self.balance -= amount

class CheckingAccount(Account):
    OVERDRAFT_LIMIT = 500.0

    @property
    def account_type(self) -> str:
        return "CHECKING"  # Directly return the type as a string
    
    def withdraw(self, amount: float):
        if self.balance - amount < -self.OVERDRAFT_LIMIT:
            raise ValueError("Exceeds overdraft limit")
        self.balance -= amount