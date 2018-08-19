from flask import Flask, Blueprint
from api import api
from resources.tocontroller import ns as todo_post_namespace

app = Flask(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = 'localhost:8888'
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    flask_app.config['RESTPLUS_VALIDATE'] = True
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = False
    flask_app.config['ERROR_404_HELP'] = False


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(todo_post_namespace)
    flask_app.register_blueprint(blueprint)


def main():
    initialize_app(app)
    app.run(debug=True)


if __name__ == "__main__":
    main()
