from app.main import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_greet_valid_user():
    client = app.test_client()
    response = client.post("/greet", json={"username": "Akarys_123"})

    assert response.status_code == 200
    assert "Hello" in response.json["message"]


def test_greet_invalid_user():
    client = app.test_client()
    response = client.post("/greet", json={"username": "<script>alert(1)</script>"})

    assert response.status_code == 400
    assert "Invalid username" in response.json["error"]


def test_calculate_add():
    client = app.test_client()
    response = client.post("/calculate", json={
        "a": 10,
        "b": 5,
        "operation": "add"
    })

    assert response.status_code == 200
    assert response.json["result"] == 15


def test_calculate_divide_by_zero():
    client = app.test_client()
    response = client.post("/calculate", json={
        "a": 10,
        "b": 0,
        "operation": "divide"
    })

    assert response.status_code == 400
    assert "division by zero" in response.json["error"]


def test_health_check():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
