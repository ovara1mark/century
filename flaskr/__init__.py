import os
from flask import Flask 
# request, abort, jsonify

# from flask_cors import CORS


from models import setup_db, Question

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    @app.route("/")
    def index():
        return "hello world"


    return app
