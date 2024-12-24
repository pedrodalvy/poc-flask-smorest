import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


def main():
    debug = os.environ.get('DEBUG', False)
    app.run(host='0.0.0.0', port=5000, debug=debug)
