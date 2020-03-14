from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
# from libs.strings import gettext
from models.user import UserModel
from schemas.user import UserSchema, UserLoginSchema
from libs.strings import gettext

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)
user_login_schema = UserLoginSchema()


class UserRegister(Resource):
    def post(self):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if UserModel.find_by_username(user.username):
            return {"message": gettext("user_username_exists")}, 400

        user.save_to_db()

        return {"message": gettext("user_registered")}, 201


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

        user = UserModel.find_by_username(user_data.username)

        if user and safe_str_cmp(user.password, user_data.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token,
                    "refresh_token": refresh_token}, 200

        return {"message": gettext("user_invalid_credentials")}, 401
