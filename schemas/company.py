from extensions import ma
from models.company import CompanyModel
from schemas.address import AddressSchema


class CompanySchema(ma.ModelSchema):
    name = ma.String()
    telephone = ma.String()
    default_off_days = ma.Int()
    address = ma.Nested(AddressSchema)
