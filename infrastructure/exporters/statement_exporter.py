import csv
from datetime import datetime
from domain.entities.statement import MonthlyStatement

class CSVStatementExporter:
    def export(self, statement: MonthlyStatement, filename: str):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Month", "Starting Balance", "Ending Balance", "Interest Earned"])
            writer.writerow([
                statement.month,
                statement.starting_balance,
                statement.ending_balance,
                statement.interest_earned
            ])


# import csv
# from reportlab.pdfgen import canvas
# from domain.entities.statement import MonthlyStatement

# class PDFStatementExporter:
#     def export(self, statement: MonthlyStatement, file_path: str):
#         pdf = canvas.Canvas(file_path)
#         pdf.drawString(100, 800, f"Monthly Statement for Account {statement.account_id}")
#         # Add more PDF formatting here
#         pdf.save()

# class CSVStatementExporter:
#     def export(self, statement: MonthlyStatement, file_path: str):
#         with open(file_path, 'w', newline='') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow(["Transaction ID", "Amount", "Type", "Timestamp"])
#             for txn in statement.transactions:
#                 writer.writerow([txn.transaction_id, txn.amount, txn.type.value, txn.timestamp])