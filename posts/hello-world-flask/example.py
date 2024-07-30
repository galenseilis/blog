from flask import Flask # 1

app = Flask(__name__) # 2

@app.route('/') # 3
def hello_world(): # 4
    return 'Hello, World' # 5

if __name__ == '__main__': # 6
    app.run(debug=True) # 7
