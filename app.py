import os

from flask import Flask
from dotenv import load_dotenv
from werkzeug.exceptions import (MethodNotAllowed, NotFound, Forbidden,
                                 Unauthorized, InternalServerError)

from resources.user import UserLogin, UserRegister, User, UserList
from extensions import jwt, db, migrate, api, ma


def create_app(script_info=None):

    app = Flask(__name__)

    load_dotenv(".env", verbose=True)
    app_settings = os.environ.get(
        "APP_SETTINGS", "config.ProductionConfig"
    )
    app.config.from_object(app_settings)

    jwt.init_app(app)
    db.init_app(app)
    api.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    api.add_resource(UserLogin, "/login")
    api.add_resource(UserRegister, "/register")
    api.add_resource(UserRegister, "/register/<string:confirmation_token>")
    api.add_resource(User, "/user/<int:user_id>")
    api.add_resource(UserList, "/users")

    @api.errorhandler(Unauthorized)
    def unauthorized_page(error):
        return {"message": "401, change this on prod."}, 401

    @api.errorhandler(Forbidden)
    def forbidden_page(error):
        return {"message": "403, change this on prod."}, 403

    @api.errorhandler(NotFound)
    def page_not_found(error):
        return {"message": "404, change this on prod."}, 404

    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {"message": "405, change this on prod."}, 405

    @api.errorhandler(InternalServerError)
    def server_error_page(error):
        return {"message": "500, change this on prod."}, 500

    return app
