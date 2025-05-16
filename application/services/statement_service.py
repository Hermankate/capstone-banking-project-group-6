from datetime import datetime

class StatementService:
    def __init__(self, transaction_repo, statement_adapter):
        self.transaction_repo = transaction_repo
        self.statement_adapter = statement_adapter

    def generate_statement(self, account_id: str, month: int, year: int, format: str):
        # Get all transactions
        transactions = self.transaction_repo.get_transactions_for_account(account_id)
        
        # Filter by month/year
        filtered = [
            txn for txn in transactions
            if txn.timestamp.month == month 
            and txn.timestamp.year == year
        ]
        
        # Generate file
        if format.lower() == "pdf":
            return self.statement_adapter.generate_pdf(filtered, account_id)
        elif format.lower() == "csv":
            return self.statement_adapter.generate_csv(filtered, account_id)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'csv'")