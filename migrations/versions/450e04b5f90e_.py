"""empty message

Revision ID: 450e04b5f90e
Revises: d4742714b6d4
Create Date: 2020-04-05 01:06:56.479750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '450e04b5f90e'
down_revision = 'd4742714b6d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmation_token', sa.String(length=36), nullable=True))
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    op.create_unique_constraint(None, 'users', ['confirmation_token'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'confirmed')
    op.drop_column('users', 'confirmation_token')
    # ### end Alembic commands ###