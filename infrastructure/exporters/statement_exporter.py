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