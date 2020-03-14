from flask_testing import TestCase

from app import create_app
from extensions import db
from models.user import UserModel

app = create_app()


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object("config.TestingConfig")
        return app

    def setUp(self):
        db.create_all()
        user = UserModel(username="test_username",
                         email="test@user.com",
                         password="test_password")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
