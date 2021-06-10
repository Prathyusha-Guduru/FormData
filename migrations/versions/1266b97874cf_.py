"""empty message

Revision ID: 1266b97874cf
Revises: 
Create Date: 2021-06-10 09:40:25.628440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1266b97874cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('waitlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_waitlist_email'), 'waitlist', ['email'], unique=True)
    op.create_index(op.f('ix_waitlist_firstname'), 'waitlist', ['firstname'], unique=True)
    op.create_index(op.f('ix_waitlist_lastname'), 'waitlist', ['lastname'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_waitlist_lastname'), table_name='waitlist')
    op.drop_index(op.f('ix_waitlist_firstname'), table_name='waitlist')
    op.drop_index(op.f('ix_waitlist_email'), table_name='waitlist')
    op.drop_table('waitlist')
    # ### end Alembic commands ###