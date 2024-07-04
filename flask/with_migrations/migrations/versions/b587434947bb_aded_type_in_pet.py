"""aded type in pet

Revision ID: b587434947bb
Revises: 89c238575fe0
Create Date: 2024-07-03 10:41:22.101468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b587434947bb'
down_revision = '89c238575fe0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pet', schema=None) as batch_op:
        batch_op.drop_column('type')

    # ### end Alembic commands ###