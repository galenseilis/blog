from flask import Flask, render_template

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


app = Flask(__name__)

@app.route('/primality/<int:number>')
def display_primarily(number):
    if is_prime(number):
        return render_template('example_is_prime.html', number=number)
    else:
        return render_template('example_is_not_prime.html', number=number)

if __name__ == '__main__':
    app.run(debug=True)
