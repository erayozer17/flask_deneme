from extensions import db


class RemainingEmployeeModel(db.Model):
    __tablename__ = "remaining_employees"

    id = db.Column(db.Integer, primary_key=True)
    no_of_remaining_employee = db.Column(db.Integer)
    admin_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    admin = db.relationship("UserModel", back_populates="employee_quota", lazy="select")

    __table_args__ = (
        db.CheckConstraint('no_of_remaining_employee >= 0', name='check_no_of_remaining_employee_positive'),
    )
