"""init  

Revision ID: 8e4526db36a6
Revises: 
Create Date: 2024-10-08 02:31:17.713047

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e4526db36a6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'points',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('basin', sa.String(200), nullable=False),
        sa.Column('lat', sa.Float(11), nullable=False),
        sa.Column('long', sa.Float(11), nullable=False),
        sa.Column('climate', sa.String(1), nullable=False),
        sa.Column('age', sa.Integer, nullable=False),
    )

def downgrade() -> None:
    op.drop_table('points')

