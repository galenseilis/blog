from flask import Flask

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist (DNE)', 404

if __name__ == '__main__':
    app.run(debug=True)
