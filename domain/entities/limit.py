from datetime import datetime
from enum import Enum

class LimitType(Enum):
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"

class TransactionLimit:
    def __init__(
        self,
        limit_type: LimitType,
        max_amount: float,
        reset_period_days: int = 1
    ):
        self.limit_type = limit_type
        self.max_amount = max_amount
        self.reset_period_days = reset_period_days
        self.last_reset = datetime.now()

    def is_exceeded(self, current_usage: float) -> bool:
        return current_usage > self.max_amount

    def needs_reset(self) -> bool:
        delta = datetime.now() - self.last_reset
        return delta.days >= self.reset_period_days

    def reset(self):
        self.last_reset = datetime.now()