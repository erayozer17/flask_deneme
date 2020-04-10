from typing import List
from uuid import uuid4
import datetime

from extensions import db

from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(128))
    email = db.Column(db.String(80), nullable=False, unique=True)
    confirmation_token = db.Column(db.String(36), unique=True, default=str(uuid4()))
    confirmed = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_manager = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    admin_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    manager_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    company = db.relationship("CompanyModel", back_populates="users", lazy="select")
    employee_quota = db.relationship("RemainingEmployeeModel", uselist=False, back_populates="admin", lazy="select")


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

    def get_remaining_employee_days(self) -> int:
        return self.employee_quota.no_of_remaining_employee

    def save_to_db(self) -> None:
        hashing_method = "pbkdf2:sha256"
        if self.password and not self.password.startswith(hashing_method):
            self.password = generate_password_hash(self.password)
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)
