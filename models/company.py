from extensions import db


class CompanyModel(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    telephone = db.Column(db.String(40), nullable=False)
    default_off_days = db.Column(db.Integer)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    users = db.relationship('UserModel', back_populates='company', lazy="select")
    address = db.relationship('AddressModel', uselist=False, back_populates='company', lazy="select")
    employee_quota = db.relationship('RemainingEmployeeModel', uselist=False, back_populates='company', lazy="select")

    __table_args__ = (
        db.CheckConstraint('default_off_days >= 0', name='check_default_off_days_positive'),
    )

    def save_to_db(self) -> int:
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        return self.id

