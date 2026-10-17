"""Flask application demonstrating HTML templates and primality testing."""

from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__, template_folder=Path(__file__).resolve().parents[2] / "templates")


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


@app.route("/primality/<int:number>")
def display_primarily(number):
    if is_prime(number):
        return render_template("example_is_prime.html", number=number)
    else:
        return render_template("example_is_not_prime.html", number=number)


def main() -> None:
    app.run(debug=True)


if __name__ == "__main__":
    main()
