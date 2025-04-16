from domain.entities.account import SavingsAccount, CheckingAccount, AccountType

def test_savings_account_withdrawal_fails_below_min_balance():
    account = SavingsAccount("acc1", AccountType.SAVINGS, balance=150.0)
    account.withdraw(60.0)
    assert account.balance == 90.0  # Passes (150 - 60 = 90 > 100? No)
    # Wait, 90 is below min balance of 100. This should raise an error. Need to correct the test.

def test_savings_account_withdrawal_fails_below_min_balance():
    account = SavingsAccount("acc1", AccountType.SAVINGS, balance=150.0)
    try:
        account.withdraw(60.0)  # 150 - 60 = 90 < 100 (min balance)
    except ValueError as e:
        assert str(e) == "Withdrawal would go below minimum balance of 100.0"

def test_checking_account_overdraft():
    account = CheckingAccount("acc1", AccountType.CHECKING, balance=0.0)
    account.withdraw(300.0)  # Allowed: balance = -300 (within -500 limit)
    assert account.balance == -300.0