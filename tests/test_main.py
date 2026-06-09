from main import app


### тест пинг понг
def test_ping():
    client = app.test_client()
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.data.decode() == 'pong'


### тест message":"Hello, World!
def test_root():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}


### тест 404
def test_not_found():
    client = app.test_client()
    response = client.get("/nonexistent")
    assert response.status_code == 404