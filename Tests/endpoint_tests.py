import requests

# Base URL of your FastAPI server
BASE_URL = "http://127.0.0.1:8000"

def test_create_account():
    payload = {
        "account_type": "SAVINGS",
        "initial_deposit": 100.0
    }
    response = requests.post(f"{BASE_URL}/accounts", json=payload)
    print("Create Account Response:", response.json())

    if response.status_code != 201:
        raise Exception(f"Failed to create account: {response.json()}")

    return response.json()["account_id"]

def test_deposit(account_id: str):
    payload = {"amount": 50.0}
    response = requests.post(f"{BASE_URL}/accounts/{account_id}/deposit", json=payload)
    print("Deposit Response:", response.json())

    if response.status_code != 200:
        raise Exception(f"Failed to deposit: {response.json()}")

def test_withdraw(account_id: str):
    payload = {"amount": 20.0}
    response = requests.post(f"{BASE_URL}/accounts/{account_id}/withdraw", json=payload)
    print("Withdraw Response:", response.json())

    if response.status_code != 200:
        raise Exception(f"Failed to withdraw: {response.json()}")

def test_get_balance(account_id: str):
    # Test fetching the account balance
    response = requests.get(f"{BASE_URL}/accounts/{account_id}/balance")
    print("Balance Response:", response.json())

def test_get_transactions(account_id: str):
    # Test fetching transaction history
    response = requests.get(f"{BASE_URL}/accounts/{account_id}/transactions")
    print("Transactions Response:", response.json())

def test_transfer_funds():
    # Test transferring funds between accounts
    payload = {
        "sourceAccountId": "acc1",
        "destinationAccountId": "acc2",
        "amount": 100.0
    }
    response = requests.post(f"{BASE_URL}/accounts/transfer", json=payload)
    print("Transfer Funds Response:", response.json())
    assert response.status_code == 200

if __name__ == "__main__":
    # Run tests in sequence
    account_id = test_create_account()
    test_deposit(account_id)
    test_withdraw(account_id)
    test_get_balance(account_id)
    test_get_transactions(account_id)
    test_transfer_funds()