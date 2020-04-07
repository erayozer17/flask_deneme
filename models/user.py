from typing import List
from uuid import uuid4

from extensions import db

from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120))
    email = db.Column(db.String(80), nullable=False, unique=True)
    confirmation_token = db.Column(db.String(36), unique=True, default=str(uuid4()))
    confirmed = db.Column(db.Boolean(), default=False)
    is_admin = db.Column(db.Boolean(), default=False)
    is_manager = db.Column(db.Boolean(), default=False)
    reports_to = db.Column(db.Integer())


    @classmethod
    def find_by_confirmation_token(cls, confirmation_token: str) -> "UserModel":
        return cls.query.filter_by(confirmation_token=confirmation_token).first()

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["UserModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def init_password_save_to_db(self) -> None:
        self.hash_password()
        self.save_to_db()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def hash_password(self) -> None:
        self.password = generate_password_hash(self.password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)
