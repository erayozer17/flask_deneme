from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from models.user import UserModel
from schemas.user import UserSchema, UserLoginSchema, UserInviteSchema, UserRegisterSchema
from libs.strings import gettext
from tasks.email import send_transactional_mail_task

from services.email import send_transactional_mail

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)
user_login_schema = UserLoginSchema()
user_invite_schema = UserInviteSchema()
user_register_schema = UserRegisterSchema()


class UserRegister(Resource):
    def post(self):
        user_json = request.get_json()

        if 'password' not in user_json:
            return {"message": gettext("user_register_password_required")}, 400

        user = user_register_schema.load(user_json)

        if UserModel.find_by_email(user.email):
            return {"message": gettext("user_email_exists")}, 400

        user.is_admin = True
        user.is_manager = True
        user.init_password_save_to_db()

        # TODO Create an html template for email.
        send_transactional_mail_task.delay(gettext("user_confirmation_subject"),
                                user.email,
                                f'<html><a href="http://localhost:5000/register/{user.confirmation_token}">Confirm</a></html>')
        
        return {"message": gettext("user_registered")}, 201

    def get(self, confirmation_token: str):
        user = UserModel.find_by_confirmation_token(confirmation_token)
        if user:
            if user.confirmed:
                return {"message": gettext("user_already_confirmed")}, 200
            user.confirmed = True
            user.save_to_db()
            if not user.password:
                # TODO use init_password_save_to_db method to hash the password
                # TODO after user returns password
                return {"message": gettext("user_password_not_set")}, 401
            return {"message": gettext("user_confirmed")}, 200
        else:
            return {"message": gettext("user_not_found")}, 404


class UserInvite(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        if not UserModel.find_by_id(current_user).confirmed:
            return {"message": gettext("user_must_confirm")}, 401
        user_json = request.get_json()
        user = user_invite_schema.load(user_json)
        user.reports_to = current_user
        user.save_to_db()

        # TODO Create an html template for email.
        send_transactional_mail_task.delay(gettext("user_confirmation_subject"),
                                user.email,
                                f'<html><a href="http://localhost:5000/register/{user.confirmation_token}">Confirm</a></html>')
        return {"message": gettext("user_invited")}, 200

class User(Resource):
    @jwt_required
    def get(self, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": gettext("user_not_found")}, 404

        return user_schema.dump(user), 200

    @jwt_required
    def delete(self, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": gettext("user_not_found")}, 404

        user.delete_from_db()
        return {"message": gettext("user_deleted")}, 200


class UserList(Resource):
    @jwt_required
    def get(self):
        return {"users": user_list_schema.dump(UserModel.find_all())}, 200


class UserLogin(Resource):
    def post(self):
        user_json = request.get_json()
        user_data = user_login_schema.load(user_json)

        user = UserModel.find_by_email(user_data.email)
        if user and user.check_password(user_data.password):
            if user.confirmed:
                access_token = create_access_token(identity=user.id, fresh=True)
                refresh_token = create_refresh_token(user.id)
                return {"access_token": access_token,
                        "refresh_token": refresh_token}, 200
            else:
                return {"message": gettext("user_not_confirmed")}, 200

        return {"message": gettext("user_invalid_credentials")}, 401
