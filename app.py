# import os

# from flask import Flask, jsonify
# from flask_restx import Api
# from flask_jwt_extended import JWTManager
# from flask_migrate import Migrate
# from marshmallow import ValidationError
# from dotenv import load_dotenv

# from db import db
# from ma import ma
# from resources.user import UserLogin#UserRegister, UserLogin, User


# app = Flask(__name__)
# app.config["DEBUG"] = True
# app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
#     "DATABASE_URI", "sqlite:///data.db"
# )
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["PROPAGATE_EXCEPTIONS"] = True
# load_dotenv(".env", verbose=True)
# api = Api(app)
# jwt = JWTManager(app)
# db.init_app(app)
# ma.init_app(app)
# migrate = Migrate(app, db)

# @app.route('/')
# def home():
#     return 'deneme'


# @app.errorhandler(ValidationError)
# def handle_marshmallow_validation(err):
#     return jsonify(err.messages), 400

# # api.add_resource(UserRegister, "/register")
# # api.add_resource(User, "/user/<int:user_id>")
# api.add_resource(UserLogin, "/login")

# if __name__ == "__main__":
#     app.run(port=5000, debug=True)





import os

from flask import Flask, jsonify
from marshmallow import ValidationError
from dotenv import load_dotenv

from resources.user import UserLogin
from extensions import jwt, db, migrate, api, ma


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URI", "sqlite:///data.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    load_dotenv(".env", verbose=True)

    # set up extensions
    jwt.init_app(app)
    db.init_app(app)
    api.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    api.add_resource(UserLogin, "/login")

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.filter(User.id == int(user_id)).first()

    # # error handlers
    # @app.errorhandler(401)
    # def unauthorized_page(error):
    #     return render_template("errors/401.html"), 401

    # @app.errorhandler(403)
    # def forbidden_page(error):
    #     return render_template("errors/403.html"), 403

    # @app.errorhandler(404)
    # def page_not_found(error):
    #     return render_template("errors/404.html"), 404

    # @app.errorhandler(500)
    # def server_error_page(error):
    #     return render_template("errors/500.html"), 500

    # # shell context for flask cli
    # @app.shell_context_processor
    # def ctx():
    #     return {"app": app, "db": db}

    return app
