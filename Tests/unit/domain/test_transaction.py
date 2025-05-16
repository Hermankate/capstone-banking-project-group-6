from domain.entities.transaction import Transaction, TransactionType


def test_transaction_creation():
    txn = Transaction("txn1", 100.0, TransactionType.DEPOSIT, account_id="acc1")
    assert txn.amount == 100.0
    assert txn.account_id == "acc1"
    assert txn.transaction_type == TransactionType.DEPOSIT