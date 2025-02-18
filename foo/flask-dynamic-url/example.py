from math import factorial

from flask import Flask

app = Flask(__name__)

@app.route('/factorial/<int:number>')
def calculate_factorial(number):
    return str(factorial(number))

if __name__ == '__main__':
    app.run(debug=True)
