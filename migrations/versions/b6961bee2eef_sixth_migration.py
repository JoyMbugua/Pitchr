"""sixth migration

Revision ID: b6961bee2eef
Revises: ea63d14327f4
Create Date: 2021-04-24 18:20:41.233071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6961bee2eef'
down_revision = 'ea63d14327f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('post', sa.String(length=255), nullable=True))
    op.drop_column('pitch', 'pitch')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('pitch', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('pitch', 'post')
    # ### end Alembic commands ###
