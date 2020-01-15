"""empty message

Revision ID: 23de523210ab
Revises: a00b4ff2fd1f
Create Date: 2020-01-12 14:25:16.901176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23de523210ab'
down_revision = 'a00b4ff2fd1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('comment', sa.String(length=300), nullable=False),
    sa.Column('posted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('comment_post_rel',
    sa.Column('post_id', sa.String(), nullable=True),
    sa.Column('comm_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['comm_id'], ['comment.public_id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], )
    )
    op.create_table('user_comment_rel',
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('comm_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['comm_id'], ['comment.public_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_comment_rel')
    op.drop_table('comment_post_rel')
    op.drop_table('comment')
    # ### end Alembic commands ###