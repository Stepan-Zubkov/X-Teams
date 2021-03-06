"""Исправление багов

Revision ID: aedbe46678af
Revises: 4f276715bd63
Create Date: 2021-08-11 19:35:44.268301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aedbe46678af'
down_revision = '4f276715bd63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('groups', sa.Column('github_url', sa.String(length=200), nullable=False))
    op.drop_column('groups', 'github')
    op.add_column('users', sa.Column('github_url', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'github_url')
    op.add_column('groups', sa.Column('github', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_column('groups', 'github_url')
    # ### end Alembic commands ###
