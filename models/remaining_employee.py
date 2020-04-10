from extensions import db


class RemainingEmployeeModel(db.Model):
    __tablename__ = "remaining_employees"

    id = db.Column(db.Integer, primary_key=True)
    no_of_remaining_employee = db.Column(db.Integer)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), unique=True)
    company = db.relationship("CompanyModel", back_populates="employee_quota", lazy="select")

    __table_args__ = (
        db.CheckConstraint('no_of_remaining_employee >= 0', name='check_no_of_remaining_employee_positive'),
    )

    def decrease_employee_quota(self):
        self.no_of_remaining_employee = self.no_of_remaining_employee - 1
        self.save_to_db()


    def save_to_db(self) -> int:
        db.session.add(self)
        db.session.commit()
