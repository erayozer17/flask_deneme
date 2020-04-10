from extensions import ma
from models.address import AddressModel


class AddressSchema(ma.ModelSchema):
    class Meta:
        model = AddressModel
        fields = ("address_line", "city", "country",)
