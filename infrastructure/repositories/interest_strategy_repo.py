from application.interfaces.interest_strategy_repo import InterestStrategyRepository
from domain.entities.interest_strategy import InterestStrategy

class InMemoryInterestStrategyRepository(InterestStrategyRepository):
    def __init__(self):
        self.strategies = {
            "simple": SimpleInterestStrategy(0.05),  # 5% annual
            "compound": CompoundInterestStrategy(0.05)
        }

    def get_strategy(self, strategy_id: str) -> InterestStrategy:
        return self.strategies.get(strategy_id)