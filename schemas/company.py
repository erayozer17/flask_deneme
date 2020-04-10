from extensions import ma
from models.company import CompanyModel
from schemas.address import AddressSchema
from schemas.remaining_employee import RemainingEmployeeSchema

class CompanySchema(ma.ModelSchema):
    class Meta:
        model = CompanyModel
        fields = ("name", "telephone", "default_off_days", "address_id",)


class CompanyLoadSchema(ma.ModelSchema):
    name = ma.String()
    telephone = ma.String()
    default_off_days = ma.Int()
    address = ma.Nested(AddressSchema)
    employee_quota = ma.Nested(RemainingEmployeeSchema)