"""Renaming name column to identification

Revision ID: 4f5f1b3c132f
Revises: 791279dd0760
Create Date: 2023-03-25 10:20:14.082047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f5f1b3c132f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("students", "name", new_column_name="identification")


def downgrade() -> None:
    op.alter_column("students", "identification", new_column_name="name")
