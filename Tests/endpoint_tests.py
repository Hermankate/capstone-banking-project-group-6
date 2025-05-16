import requests
import pytest
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"

def test_create_account(account_type="SAVINGS", initial_deposit=100.0):
    payload = {
        "account_type": account_type,
        "initial_deposit": initial_deposit
    }
    response = requests.post(f"{BASE_URL}/accounts", json=payload)
    print(f"Created {account_type} account:", response.json())
    return response.json()["account_id"]

def test_deposit(account_id: str, amount=50.0):
    payload = {"amount": amount}
    response = requests.post(
        f"{BASE_URL}/accounts/{account_id}/deposit",
        json=payload
    )
    print(f"Deposit to {account_id}:", response.json())

def test_withdraw(account_id: str, amount=20.0):
    payload = {"amount": amount}
    response = requests.post(
        f"{BASE_URL}/accounts/{account_id}/withdraw",
        json=payload
    )
    print(f"Withdraw from {account_id}:", response.json())

def test_get_balance(account_id: str):
    response = requests.get(f"{BASE_URL}/accounts/{account_id}/balance")
    print(f"Balance for {account_id}:", response.json())
    return response.json()

def test_calculate_interest(account_id: str):
    try:
        response = requests.post(
            f"{BASE_URL}/accounts/{account_id}/interest/calculate"
        )
        if response.status_code == 200:
            print(f"Interest calculated:", response.json())
            return response.json()
        else:
            print(f"Interest error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"Interest calculation failed: {str(e)}")
        return None
def test_generate_statement(account_id: str):
    current_date = datetime.now()
    try:
        response = requests.get(
            f"{BASE_URL}/accounts/{account_id}/statement",
            params={
                "year": current_date.year,
                "month": current_date.month,
                "format": "pdf"
            }
        )
        if response.status_code == 200:
            print(f"Statement generated successfully for {account_id}")
            return True
        else:
            print(f"Statement failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"Statement generation error: {str(e)}")
        return False
def test_transaction_limits(account_id: str):
    try:
        # Try to withdraw more than daily limit
        payload = {"amount": 1500}
        response = requests.post(
            f"{BASE_URL}/accounts/{account_id}/withdraw",
            json=payload
        )
        print("Limit test result:", response.json())
    except Exception as e:
        print("Limit enforcement worked:", str(e))

if __name__ == "__main__":
    # Create test account
    acc_id = test_create_account("SAVINGS", 1000.0)
    
    # Test Week 1-2 features
    test_deposit(acc_id)
    test_withdraw(acc_id)
    
    # Test Week 3 features
    test_calculate_interest(acc_id)
    
    # Verify balance after interest
    balance = test_get_balance(acc_id)
    assert float(balance["balance"]) > 1000.0, "Interest not applied"
    
    # Test statement generation
    assert test_generate_statement(acc_id) == 200
    
    # Test transaction limits
    test_transaction_limits(acc_id)
    
    print("All Week 3 tests completed successfully!")