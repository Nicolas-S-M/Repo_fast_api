from http import HTTPStatus


def test_read_root_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Ola mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'name': 'nicolas',
            'age': 20,
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'name': 'nicolas', 'age': 20, 'id': 1}


def test_read_user(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'name': 'nicolas',
                'age': 20,
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'name': 'nicolas2',
            'age': 22,
            'id': 1,
        },
    )
    if response.status_code == HTTPStatus.NOT_FOUND:
        assert response.json() == {'detail': 'User not found'}
    assert response.json() == {
        'name': 'nicolas2',
        'age': 22,
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    if response.status_code == HTTPStatus.NOT_FOUND:
        assert response.json() == {'detail': 'User not found'}
    assert response.json() == {'message': 'User deleted'}
