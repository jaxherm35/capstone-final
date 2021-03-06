"""updated user table

Revision ID: f0e7bd216259
Revises: 86e7e55bbcaf
Create Date: 2022-07-20 15:38:34.969721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0e7bd216259'
down_revision = '86e7e55bbcaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('password', sa.String(length=25), nullable=True))
    op.drop_constraint('user_name_key', 'user', type_='unique')
    op.create_unique_constraint(None, 'user', ['username'])
    op.drop_column('user', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_unique_constraint('user_name_key', 'user', ['name'])
    op.drop_column('user', 'password')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
