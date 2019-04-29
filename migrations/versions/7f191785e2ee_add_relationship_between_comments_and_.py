"""add relationship between comments and posts

Revision ID: 7f191785e2ee
Revises: 85cfb1f06abf
Create Date: 2019-04-29 22:00:59.850926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f191785e2ee'
down_revision = '85cfb1f06abf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment_date', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'comments', 'posts', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'comment_date')
    # ### end Alembic commands ###