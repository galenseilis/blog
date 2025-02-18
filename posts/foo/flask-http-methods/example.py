import getpass

from flask import Flask, request

app = Flask(__name__)

@app.route('/automorphisms', methods=['GET', 'POST'])
def http_methods_example():
    if request.method == 'GET':
        return '<iframe width="560" height="315" src="https://www.youtube.com/embed/vY1UkCPSKH8?si=mRB5eM30UmTUVfhv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    if request.method == 'POST':
        return 'POST'
    # We don't need to bother with PUT and DELETE

if __name__ == '__main__':
    app.run(debug=True)
