"""Flask application demonstrating dynamic URLs to compute factorials."""

from math import factorial

from flask import Flask

app = Flask(__name__)


@app.route("/factorial/<int:number>")
def calculate_factorial(number):
    return str(factorial(number))


def main() -> None:
    app.run(debug=True)


if __name__ == "__main__":
    main()
