"""empty message

Revision ID: fae953cefba6
Revises: d19811c4d316
Create Date: 2022-06-27 14:07:16.186427

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fae953cefba6'
down_revision = 'd19811c4d316'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.String(length=50), nullable=False))
    op.add_column('users', sa.Column('profile_photo', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('role', sa.String(length=15), nullable=False))
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)
    op.alter_column('users', 'password',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
    op.drop_column('users', 'role')
    op.drop_column('users', 'profile_photo')
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###
