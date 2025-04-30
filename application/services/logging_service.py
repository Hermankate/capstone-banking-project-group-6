# application/services/logging_service.py
import logging

from domain.entities.transaction import Transaction

logging.basicConfig(filename='transactions.log', level=logging.INFO)

def log_transaction(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        transaction = result if isinstance(result, Transaction) else None
        if transaction:
            logging.info(
                f"{transaction.type.value}: "
                f"Amount: {transaction.amount}, "
                f"Source: {transaction.source_account_id}, "
                f"Destination: {transaction.destination_account_id or 'N/A'}"
            )
        return result
    return wrapper