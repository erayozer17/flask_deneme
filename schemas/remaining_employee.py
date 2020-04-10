from extensions import ma
from models.remaining_employee import RemainingEmployeeModel
from schemas.user import UserSchema


class RemainingEmployeeSchema(ma.ModelSchema):
    no_of_remaining_employee = ma.String()
    admin = ma.Nested(UserSchema)