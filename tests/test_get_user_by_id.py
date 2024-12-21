from http import HTTPStatus

from fastapi.testclient import TestClient

from tests.fixtures.data import USERS_FIXTURE_1


def test_get_user_by_id(test_client: TestClient, db_with_users_1):
    response = test_client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['id'] == 1
    assert data['username'] == USERS_FIXTURE_1[0]['username']
    assert data['email'] == USERS_FIXTURE_1[0]['email']
    assert 'password' not in data


def test_get_user_by_id_with_status_not_found(test_client: TestClient):
    response = test_client.get('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    data = response.json()
    assert data['detail'] == 'User not found.'
