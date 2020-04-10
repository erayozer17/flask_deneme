from extensions import ma
from models.address import AddressModel


class AddressSchema(ma.ModelSchema):
    address_line = ma.String()
    city = ma.String()
    country = ma.String()