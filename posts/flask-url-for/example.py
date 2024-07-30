import requests
import io

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/card/<int:card_id>')
def card(card_id):
    return f'Card({card_id})'

with app.test_request_context():
    for i in range(10):
        print(url_for('card', card_id=str(i)))

if __name__ == '__main__':
    app.run(debug=True)
