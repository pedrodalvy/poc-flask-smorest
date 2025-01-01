import importlib.metadata
import os

from flask import Flask
from flask_smorest import Api

from src.routes.authors import authors_blp
from src.routes.posts import posts_blp

app = Flask(__name__)

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = importlib.metadata.version("poc-flask-smorest")
app.config["OPENAPI_VERSION"] = "3.0.2"

api = Api(app)
api.register_blueprint(authors_blp)
api.register_blueprint(posts_blp)


def main():
    debug = os.environ.get("DEBUG", False)
    app.run(host="0.0.0.0", port=5000, debug=debug)
