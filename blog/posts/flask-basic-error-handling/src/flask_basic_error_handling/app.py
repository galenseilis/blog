"""Flask application demonstrating basic error handling."""

from flask import Flask

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return "This page does not exist (DONE)", 404


def main() -> None:
    app.run(debug=True)


if __name__ == "__main__":
    main()
