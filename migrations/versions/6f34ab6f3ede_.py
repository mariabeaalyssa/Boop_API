"""empty message

Revision ID: 6f34ab6f3ede
Revises: 14771996a7d0
Create Date: 2020-01-14 02:18:46.679624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f34ab6f3ede'
down_revision = '14771996a7d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('posted_by', sa.String(), nullable=True))
    op.create_foreign_key(None, 'comment', 'user', ['posted_by'], ['username'])
    op.add_column('deal', sa.Column('deal_owner', sa.String(), nullable=True))
    op.create_foreign_key(None, 'deal', 'user', ['deal_owner'], ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'deal', type_='foreignkey')
    op.drop_column('deal', 'deal_owner')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'posted_by')
    # ### end Alembic commands ###