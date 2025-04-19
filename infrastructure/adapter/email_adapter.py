# infrastructure/adapters/email_adapter.py
class EmailAdapter:
    def send_email(self, recipient, message):
        print(f"Email to {recipient}: {message}")

# infrastructure/adapters/sms_adapter.py
class SMSAdapter:
    def send_sms(self, number, message):
        print(f"SMS to {number}: {message}")