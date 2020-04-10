import os

from flask import Flask
from dotenv import load_dotenv
from werkzeug.exceptions import (MethodNotAllowed, NotFound, Forbidden,
                                 Unauthorized, InternalServerError)

from resources.user import UserLogin, UserRegister, User, UserList, UserInvite
from extensions import jwt, db, migrate, api, ma, celery, mail


def create_app(script_info=None):

    app = Flask(__name__)

    load_dotenv(".env", verbose=True)
    app_settings = os.environ.get("APP_SETTINGS")
    if not app_settings:
        raise ValueError('APP_SETTINGS environment variable is not set. Aborting.')
    app.config.from_object(app_settings)

    #Migration purposes
    from models import user, remaining_employee, company, address

    jwt.init_app(app)
    db.init_app(app)
    api.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    init_celery(app)
    mail.init_app(app)

    api.add_resource(UserLogin, "/login")
    api.add_resource(UserRegister, "/register")
    api.add_resource(UserRegister, "/register/<string:confirmation_token>")
    api.add_resource(User, "/user/<int:user_id>")
    api.add_resource(UserList, "/users")
    api.add_resource(UserInvite, "/invite")

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

def init_celery(app=None):
    app = app or create_app()
    celery.conf.broker_url = app.config["CELERY_BROKER_URL"]
    celery.conf.result_backend = app.config["CELERY_RESULT_BACKEND"]
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        """Make celery tasks work with Flask app context"""

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

