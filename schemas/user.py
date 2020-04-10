from extensions import ma
from models.user import UserModel
from schemas.company import CompanySchema

from copy import deepcopy


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)
        ordered = True
    company = ma.Nested(CompanySchema)


class UserLoginSchema(ma.ModelSchema):
    email = ma.String()
    password = ma.String()


class UserInviteSchema(ma.ModelSchema):
    email = ma.String()
    name = ma.String()
    surname = ma.String()
    is_manager = ma.Boolean()


class UserRegisterSchema(ma.ModelSchema):
    email = ma.String()
    name = ma.String()
    surname = ma.String()
    password = ma.String()
    company = ma.Nested(CompanySchema)


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
