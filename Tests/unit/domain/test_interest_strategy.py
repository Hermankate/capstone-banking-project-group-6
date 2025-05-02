# tests/unit/domain/test_interest_strategy.py
from domain.entities.interest_strategy import SimpleInterestStrategy
from domain.entities.limit import LimitType, TransactionLimit


def test_simple_interest():
    strategy = SimpleInterestStrategy(0.05)  # 5% annual rate
    interest = strategy.calculate_interest(1000.0, 365)  # 1 year
    assert interest == 50.0  # 1000 * 0.05

# tests/unit/application/test_limit_service.py
def test_limit_exceeded():
    limit = TransactionLimit(LimitType.DAILY, 500.0)
    assert limit.is_exceeded(600.0) is True