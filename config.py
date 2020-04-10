import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = os.getenv("APP_NAME", "ingrydHR_backend")
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    DEBUG = True
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    MAIL_DEFAULT_SENDER = 'test@ingrydhr.com'


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URI",
        "sqlite:///{0}".format(os.path.join(basedir, "dev.db"))
    )
    CELERY_BROKER_URL = os.environ.get("DEV_CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = os.environ.get("DEV_CELERY_RESULT_BACKEND")


class TestingConfig(BaseConfig):
    """Testing configuration."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""

    SQLALCHEMY_DATABASE_URI = os.environ["PROD_DATABASE_URI"]
    CELERY_BROKER_URL = os.environ["PROD_CELERY_BROKER_URL"]
    CELERY_RESULT_BACKEND = os.environ["PROD_CELERY_RESULT_BACKEND"]
    DEBUG = False

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
