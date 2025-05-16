class MockNotificationAdapter:
    def send(self, recipient, message):
        print(f"Notification sent to {recipient}: {message}")