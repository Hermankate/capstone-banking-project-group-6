import csv
from reportlab.pdfgen import canvas
from pathlib import Path

class StatementAdapter:
    def generate_pdf(self, transactions, account_id: str):
        filename = f"statement_{account_id}.pdf"
        pdf = canvas.Canvas(filename)
        y = 800
        for txn in transactions:
            pdf.drawString(100, y, 
                f"{txn.timestamp} - {txn.transaction_type.value}: ${txn.amount}"
            )
            y -= 20
        pdf.save()
        return filename

    def generate_csv(self, transactions, account_id: str):
        filename = f"statement_{account_id}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Amount"])
            for txn in transactions:
                writer.writerow([
                    txn.timestamp.isoformat(),
                    txn.transaction_type.value,
                    txn.amount
                ])
        return filename