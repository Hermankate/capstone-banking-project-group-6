import logging

class LoggingService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def log_transaction(self, transaction):
        self.logger.info(f"Transaction {transaction.transaction_id}: {transaction.transaction_type} of {transaction.amount}")