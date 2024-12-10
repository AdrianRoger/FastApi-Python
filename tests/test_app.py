from http import HTTPStatus

from fastapi.testclient import TestClient

from crud_fastapi.app import app


def test_hello_world():
    client = TestClient(app)  # Arrange (organizar)

    response = client.get('/hello-world')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assertion
    assert response.json() == {'message': 'hello world'} # Assertion
