"""empty message

Revision ID: e11d8fe0eb74
Revises: 1358c49f3cc0
Create Date: 2022-03-21 16:00:13.175184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e11d8fe0eb74'
down_revision = '1358c49f3cc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classroom_booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(length=400), nullable=False),
    sa.Column('book_details', sa.String(length=500), nullable=False),
    sa.Column('date_of_booking', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('order')
    op.drop_table('order_item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_item',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name='order_item_order_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='order_item_pkey')
    )
    op.create_table('order',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_open', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='order_pkey')
    )
    op.drop_table('classroom_booking')
    # ### end Alembic commands ###
