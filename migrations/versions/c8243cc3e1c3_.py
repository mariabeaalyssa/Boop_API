"""empty message

Revision ID: c8243cc3e1c3
Revises: 
Create Date: 2020-01-19 22:02:43.639119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8243cc3e1c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('deal', sa.Column('pet_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'deal', 'pet', ['pet_id'], ['public_id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'deal', type_='foreignkey')
    op.drop_column('deal', 'pet_id')
    # ### end Alembic commands ###
