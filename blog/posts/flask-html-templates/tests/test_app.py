from flask_html_templates.app import app, is_prime


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(9) is False
    assert is_prime(1) is False


def test_prime_route():
    client = app.test_client()
    response = client.get('/primality/2')
    assert response.status_code == 200
    assert b'prime' in response.data
