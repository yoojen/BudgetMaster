from api.bm.views import bm_views
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import session
from models import *
from models.user import User

app = Flask(__name__)
app.register_blueprint(bm_views)
cors = CORS(app, resources={r"api/bm/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    session.close()


@app.route('/', strict_slashes=False)
def homeroute():
    return "hello"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
