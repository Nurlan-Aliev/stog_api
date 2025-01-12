"""empty message

Revision ID: a9c7f7e94f2b
Revises: c6a886ea03b0
Create Date: 2024-08-21 00:28:56.121233

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9c7f7e94f2b'
down_revision: Union[str, None] = 'c6a886ea03b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('storehalls',
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('stockhalls')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stockhalls',
    sa.Column('name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='stockhalls_pkey')
    )
    op.drop_table('storehalls')
    # ### end Alembic commands ###
