from flask_basic_error_handling.app import app, page_not_found


def test_page_not_found_returns_404():
    client = app.test_client()
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'This page does not exist (DONE)' in response.data
