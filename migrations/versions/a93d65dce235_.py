"""empty message

Revision ID: a93d65dce235
Revises: 
Create Date: 2023-11-21 19:41:16.459971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a93d65dce235'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('sweet_product',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trace_id', sa.String(), nullable=True),
    sa.Column('price_sweet', sa.Float(), nullable=False),
    sa.Column('weight_sweet', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('trace_id')
    )
    op.create_table('sweet_product_to_ingredient',
    sa.Column('id_sweet_product', sa.Integer(), nullable=False),
    sa.Column('id_ingredient', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_ingredient'], ['ingredient.id'], ),
    sa.ForeignKeyConstraint(['id_sweet_product'], ['sweet_product.id'], ),
    sa.PrimaryKeyConstraint('id_sweet_product', 'id_ingredient')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trace_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('surname', sa.String(length=32), nullable=False),
    sa.Column('patronymics', sa.String(length=32), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('data_bith', sa.Date(), nullable=True),
    sa.Column('passport_series', sa.String(length=4), nullable=True),
    sa.Column('passport_number', sa.String(length=10), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('trace_id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trace_id', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('datatime_order', sa.DateTime(), nullable=False),
    sa.Column('type_order', sa.Enum('in_hall', 'with_myself', name='typeorder'), nullable=True),
    sa.Column('status_order', sa.Enum('waiting_for_payment', 'paid', 'waiting_for_confirmation', 'confirmed', 'prepared', 'ready', 'waiting_for_the_courier', 'delivery', 'completed', name='statusorder'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('trace_id')
    )
    op.create_table('order_to_sweet_product',
    sa.Column('id_order', sa.Integer(), nullable=False),
    sa.Column('id_sweet_product', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['id_order'], ['order.id'], ),
    sa.ForeignKeyConstraint(['id_sweet_product'], ['sweet_product.id'], ),
    sa.PrimaryKeyConstraint('id_order', 'id_sweet_product')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_to_sweet_product')
    op.drop_table('order')
    op.drop_table('users')
    op.drop_table('sweet_product_to_ingredient')
    op.drop_table('sweet_product')
    op.drop_table('role')
    op.drop_table('ingredient')
    # ### end Alembic commands ###
