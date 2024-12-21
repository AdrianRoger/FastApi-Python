from http import HTTPStatus

from fastapi.testclient import TestClient


def test_create_user(test_client: TestClient):
    response = test_client.post(
        '/users/',
        json={
            'username': 'Usuário de testes',
            'email': 'user_tester@example.com',
            'password': 'securepassword',
        },
    )  # Act (ação)

    assert response.status_code == HTTPStatus.CREATED  # Assertion
    response_data = response.json()
    user_id = response_data['id']

    assert response_data == {
        'id': user_id,
        'username': 'Usuário de testes',
        'email': 'user_tester@example.com',
    }  # Assertion
    # TODO : Criar os demais Testes
