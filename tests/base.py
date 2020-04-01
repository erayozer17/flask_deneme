from time import sleep
from os import remove

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

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        sleep(0.1)
        remove("test.db")

    def create_user(self, username="test_username",
                    email="test@user.com", password="test_password"):
        user = UserModel(username=username,
                         email=email,
                         password=password)
        db.session.add(user)
        db.session.commit()
