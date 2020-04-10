from extensions import ma
from models.user import UserModel
from schemas.company import CompanyLoadSchema

from copy import deepcopy


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password", "confirmation_token", "created_at",)
        dump_only = ("id",)
        ordered = True
    company = ma.Nested(CompanyLoadSchema)


class UserLoginSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        fields = ("email", "password",)


class UserInviteSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        fields = ("email", "is_manager",)


class UserRegisterSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        fields = ("email", "name", "surname", "password", "company_id",)


def partial_schema_factory(schema_cls, partial=True, many=False):
    schema = schema_cls(partial=partial)
    for field_name, field in schema.fields.items():
        if isinstance(field, ma.Nested):
            _whatever_its_doing(field, schema, partial, field_name, many)
    return schema


def _whatever_its_doing(field, schema, partial, field_name, many):
    new_field = deepcopy(field)
    new_field.schema.partial = partial
    new_field.schema.many = many
    schema.fields[field_name] = new_field
