from domain.entities.transaction import Transaction, TransactionType

def test_transaction_creation():
    txn = Transaction("txn1", "acc1", 100.0, TransactionType.DEPOSIT)
    assert txn.amount == 100.0
    assert txn.type == TransactionType.DEPOSIT