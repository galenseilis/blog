from flask_http_methods.app import app, http_methods_example


def test_http_methods_example_is_callable():
    assert callable(http_methods_example)


def test_get_returns_iframe():
    client = app.test_client()
    response = client.get('/automorphisms')
    assert response.status_code == 200
    assert b'iframe' in response.data


def test_post_returns_post():
    client = app.test_client()
    response = client.post('/automorphisms')
    assert response.status_code == 200
    assert b'POST' in response.data
