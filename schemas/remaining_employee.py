from extensions import ma


class RemainingEmployeeSchema(ma.ModelSchema):
    no_of_remaining_employee = ma.String()
