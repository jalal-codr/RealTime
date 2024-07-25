import os
from flask import Flask, request
from flask_cors import CORS
# from .Routes.routes  import bp as routes


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app,resources={r"/*":{"origin":"*"}})

    UPLOAD_FOLDER = 'uploads/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    from .Routes.routes  import bp as routes
    app.register_blueprint(routes)

    return app