from extensions import ma
from models.remaining_employee import RemainingEmployeeModel


class RemainingEmployeeSchema(ma.ModelSchema):
    no_of_remaining_employee = ma.String()
