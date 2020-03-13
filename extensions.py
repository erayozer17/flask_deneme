from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()
api = Api()
ma = Marshmallow()