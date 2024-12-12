from http import HTTPStatus

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

TEST_DATABASE_URL = 'sqlite:///./memory.db'


engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


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
