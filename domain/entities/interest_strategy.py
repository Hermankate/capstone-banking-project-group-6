from abc import ABC, abstractmethod

class InterestStrategy(ABC):
    @abstractmethod
    def calculate_interest(self, balance: float, days: int) -> float:
        pass

class SimpleInterestStrategy(InterestStrategy):
    def __init__(self, annual_rate: float):
        self.annual_rate = annual_rate

    def calculate_interest(self, balance: float, days: int) -> float:
        return balance * self.annual_rate * (days / 365)

class CompoundInterestStrategy(InterestStrategy):
    def __init__(self, annual_rate: float, compounding_frequency: int = 12):
        self.annual_rate = annual_rate
        self.compounding_frequency = compounding_frequency

    def calculate_interest(self, balance: float, days: int) -> float:
        periods = days / (365 / self.compounding_frequency)
        return balance * (1 + self.annual_rate / self.compounding_frequency) ** periods - balance