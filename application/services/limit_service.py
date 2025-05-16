class LimitEnforcementService:
    def check_daily_limit(self, account, amount):
        if account.daily_used + amount > account.daily_limit:
            raise ValueError("Exceeds daily limit")
        
    def check_monthly_limit(self, account, amount):
        if account.monthly_used + amount > account.monthly_limit:
            raise ValueError("Exceeds monthly limit")
        
    def reset_limits(self):
        # Call this daily/monthly via cron job
        pass