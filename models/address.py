from extensions import db


class AddressModel(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True)
    address_line = db.Column(db.String(256))
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    company = db.relationship('CompanyModel', uselist=False, back_populates='address', lazy="select")

    def save_to_db(self) -> int:
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        return self.id
