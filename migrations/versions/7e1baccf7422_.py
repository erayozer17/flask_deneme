"""empty message

Revision ID: 7e1baccf7422
Revises: 
Create Date: 2020-04-09 21:31:01.554669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e1baccf7422'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address_line', sa.String(length=256), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('telephone', sa.String(length=40), nullable=False),
    sa.Column('default_off_days', sa.Integer(), nullable=True),
    sa.CheckConstraint('default_off_days >= 0', name='check_default_off_days_positive'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('remaining_employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('no_of_remaining_employee', sa.Integer(), nullable=True),
    sa.CheckConstraint('no_of_remaining_employee >= 0', name='check_no_of_remaining_employee_positive'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('surname', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('confirmation_token', sa.String(length=36), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_manager', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('confirmation_token'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('remaining_employees')
    op.drop_table('companies')
    op.drop_table('addresses')
    # ### end Alembic commands ###