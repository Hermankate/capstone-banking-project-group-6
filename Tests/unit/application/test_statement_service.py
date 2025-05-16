from application.services.statement_service import StatementService
from application.services.statement_adapter import StatementAdapter
from infrastructure.repositories.transaction_repository_impl import InMemoryTransactionRepository
from domain.entities.transaction import Transaction, TransactionType

def test_generate_pdf_and_csv(tmp_path):
    repo = InMemoryTransactionRepository()
    adapter = StatementAdapter()
    service = StatementService(repo, adapter)
    txn = Transaction("txn1", 100, TransactionType.DEPOSIT, account_id="acc1")
    repo.save_transaction(txn)
    pdf_file = service.generate_statement("acc1", txn.timestamp.month, txn.timestamp.year, "pdf")
    csv_file = service.generate_statement("acc1", txn.timestamp.month, txn.timestamp.year, "csv")
    assert pdf_file.endswith(".pdf")
    assert csv_file.endswith(".csv")