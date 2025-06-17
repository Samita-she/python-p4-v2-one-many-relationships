"""Add employee_id foreign key to Review

Revision ID: 1614ceab4ece
Revises: c390e5c9d021
Create Date: 2025-06-17 19:47:23.108668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1614ceab4ece'
down_revision = 'c390e5c9d021'
branch_labels = None
depends_on = None  
def upgrade():
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_reviews_employee_id_employees',  # use a descriptive name
            'employees',
            ['employee_id'],
            ['id']
        )
def downgrade():
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')
