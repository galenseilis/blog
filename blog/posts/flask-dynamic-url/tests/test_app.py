from flask_dynamic_url.app import app, calculate_factorial


def test_calculate_factorial():
    assert calculate_factorial(0) == '1'
    assert calculate_factorial(5) == '120'


def test_factorial_route():
    client = app.test_client()
    response = client.get('/factorial/5')
    assert response.status_code == 200
    assert b'120' in response.data
