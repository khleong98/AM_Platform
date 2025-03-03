"""Initial

Revision ID: dd9624a7dc74
Revises: 
Create Date: 2024-05-13 11:43:30.946433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd9624a7dc74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('referrer_id', sa.Integer(), nullable=True),
    sa.Column('point', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['referrer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('referral',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('referrer_id', sa.Integer(), nullable=False),
    sa.Column('referree_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['referree_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['referrer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('referree_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('referral')
    op.drop_table('user')
    # ### end Alembic commands ###
