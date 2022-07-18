"""updated db

Revision ID: 86e7e55bbcaf
Revises: 2752a3636feb
Create Date: 2022-07-18 16:21:20.361643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86e7e55bbcaf'
down_revision = '2752a3636feb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homeowner',
    sa.Column('homeowner_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('address', sa.String(length=80), nullable=True),
    sa.Column('phone_number', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('avg_bill', sa.String(length=80), nullable=True),
    sa.Column('total_kwh', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('homeowner_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('sits',
    sa.Column('sit_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('homeowner_id', sa.Integer(), nullable=True),
    sa.Column('new_price_with', sa.Integer(), nullable=True),
    sa.Column('new_price_without', sa.Integer(), nullable=True),
    sa.Column('offset', sa.Integer(), nullable=True),
    sa.Column('panels', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=300), nullable=True),
    sa.ForeignKeyConstraint(['homeowner_id'], ['homeowner.homeowner_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('sit_id')
    )
    op.create_table('sold',
    sa.Column('sold_id', sa.Integer(), nullable=False),
    sa.Column('sit_id', sa.Integer(), nullable=True),
    sa.Column('new_price_with', sa.Integer(), nullable=True),
    sa.Column('new_price_without', sa.Integer(), nullable=True),
    sa.Column('offset', sa.Integer(), nullable=True),
    sa.Column('panels', sa.Integer(), nullable=True),
    sa.Column('loan_provider', sa.String(length=80), nullable=True),
    sa.Column('interest_rate', sa.String(length=10), nullable=True),
    sa.Column('re_roof', sa.Boolean(), nullable=True),
    sa.Column('date_sold', sa.String(length=30), nullable=True),
    sa.Column('notes', sa.String(length=300), nullable=True),
    sa.ForeignKeyConstraint(['sit_id'], ['sits.sit_id'], ),
    sa.PrimaryKeyConstraint('sold_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sold')
    op.drop_table('sits')
    op.drop_table('user')
    op.drop_table('homeowner')
    # ### end Alembic commands ###