"""empty message

Revision ID: 05677086f974
Revises: 55d9ea132c57
Create Date: 2023-02-07 08:02:12.007144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05677086f974'
down_revision = '55d9ea132c57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('date', sa.String(length=120), nullable=False),
    sa.Column('time', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=360), nullable=False),
    sa.Column('location', sa.String(length=240), nullable=False),
    sa.Column('guests', sa.String(length=240), nullable=False),
    sa.Column('image', sa.String(length=360), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###
