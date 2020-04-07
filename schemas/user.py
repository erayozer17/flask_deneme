from extensions import ma
from models.user import UserModel

# from werkzeug.security import generate_password_hash


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)


class UserLoginSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        fields = ("email", "password")


class UserInviteSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        fields = ("email", "name", "surname", "is_manager")


class UserRegisterSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        fields = ("email", "name", "surname", "password")
    # password = generate_password_hash()
