from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_existing_branch():
    response = client.get("/branches/ABHY0065001")
    assert response.status_code == 200
    data = response.json()
    assert data["ifsc"] == "ABHY0065001"
    assert "address" in data
    assert data["city"] == "MUMBAI"

def test_get_nonexistent_branch():
    response = client.get("/branches/INVALIDIFSC1234")
    assert response.status_code in (404, 200)  # depending on your app logic
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Branch not found"

def test_get_all_branches():
    response = client.get("/branches")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    # Check if at least one branch has the expected keys
    sample = data[0]
    assert "ifsc" in sample
    assert "address" in sample
    assert "city" in sample

def test_search_branches_by_bank_city():
    # Assuming your API supports query parameters for searching e.g. /branches?city=MUMBAI
    response = client.get("/branches?city=MUMBAI")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for branch in data:
        assert "MUMBAI" in branch["city"] or "MUMBAI" in branch.get("city", "")

def test_branch_response_structure():
    response = client.get("/branches/ABHY0065001")
    assert response.status_code == 200
    data = response.json()
    # Check keys exist and types
    expected_keys = {
        "ifsc": str,
        "bank_id": int,
        "branch": str,
        "address": str,
        "city": str,
        "district": str,
        "state": str,
    }
    for key, typ in expected_keys.items():
        assert key in data
        assert isinstance(data[key], typ)

def test_invalid_ifsc_format():
    # IFSC codes usually follow a specific format (e.g. 4 letters + 7 digits)
    response = client.get("/branches/123INVALIDIFSC")
    assert response.status_code == 404 or response.status_code == 400
    data = response.json()
    assert "detail" in data

def test_get_branches_pagination():
    # If your API supports pagination via query parameters like ?limit=10&offset=5
    response = client.get("/branches?limit=5&offset=0")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 5

def test_method_not_allowed():
    # Trying POST on a GET-only endpoint
    response = client.post("/branches/ABHY0065001")
    assert response.status_code == 405  # Method Not Allowed
    data = response.json()
    assert "detail" in data

