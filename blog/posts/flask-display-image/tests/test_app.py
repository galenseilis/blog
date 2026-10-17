from flask_display_image.app import display_image


def test_display_image_is_callable():
    assert callable(display_image)
