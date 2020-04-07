from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from celery import Celery

jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()
api = Api()
ma = Marshmallow()
celery = Celery()
mail = Mail()
