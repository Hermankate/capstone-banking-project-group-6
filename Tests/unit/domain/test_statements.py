# tests/integration/test_statements.py
def test_generate_statement(client):
    response = client.post(
        "/statements/generate",
        json={"account_id": "acc1", "month": 10, "year": 2023, "format": "csv"}
    )
    assert response.status_code == 200
    assert "generated" in response.json()["message"]