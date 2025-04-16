# application/services/notification_service.py
from abc import ABC, abstractmethod

class NotificationObserver(ABC):
    @abstractmethod
    def notify(self, transaction):
        pass

class EmailNotification(NotificationObserver):
    def notify(self, transaction):
        # Simulate sending email
        print(f"Email: Transaction {transaction.transaction_id} completed!")

class SMSNotification(NotificationObserver):
    def notify(self, transaction):
        # Simulate sending SMS
        print(f"SMS: Transaction {transaction.transaction_id} completed!")

class NotificationService:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: NotificationObserver):
        self.observers.append(observer)

    def notify_all(self, transaction):
        for observer in self.observers:
            observer.notify(transaction)