"""created_game_model

Revision ID: fc0588d839b7
Revises: 6406b166c89c
Create Date: 2024-07-09 16:13:48.045491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc0588d839b7'
down_revision = '6406b166c89c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('member_id', sa.BigInteger(), nullable=False),
    sa.Column('board', sa.Text(), nullable=False),
    sa.Column('knight_x', sa.Integer(), nullable=False),
    sa.Column('knight_y', sa.Integer(), nullable=False),
    sa.Column('rook_x', sa.Integer(), nullable=False),
    sa.Column('rook_y', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('member_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###