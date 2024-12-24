import importlib.metadata
import os

from flask import Flask
from flask_smorest import Api

app = Flask(__name__)

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = importlib.metadata.version('poc-flask-smorest')
app.config["OPENAPI_VERSION"] = "3.0.2"

api = Api(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


def main():
    debug = os.environ.get('DEBUG', False)
    app.run(host='0.0.0.0', port=5000, debug=debug)
