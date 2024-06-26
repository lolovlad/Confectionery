"""empty message

Revision ID: 03631012718e
Revises: 
Create Date: 2024-05-13 11:22:26.488645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03631012718e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bakery',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trace_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bakery')),
    sa.UniqueConstraint('trace_id', name=op.f('uq_bakery_trace_id'))
    )
    op.create_table('ingredient',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_ingredient'))
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_role')),
    sa.UniqueConstraint('name', name=op.f('uq_role_name'))
    )
    op.create_table('type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_type'))
    )
    op.create_table('sweet_product',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trace_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('price_sweet', sa.Float(), nullable=False),
    sa.Column('weight_sweet', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['type.id'], name=op.f('fk_sweet_product_type_id_type')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_sweet_product')),
    sa.UniqueConstraint('trace_id', name=op.f('uq_sweet_product_trace_id'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trace_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('surname', sa.String(length=32), nullable=False),
    sa.Column('patronymics', sa.String(length=32), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=32), nullable=False),
    sa.Column('data_bith', sa.Date(), nullable=True),
    sa.Column('passport_series', sa.String(length=4), nullable=True),
    sa.Column('passport_number', sa.String(length=10), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], name=op.f('fk_users_role_id_role')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('trace_id', name=op.f('uq_users_trace_id'))
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trace_id', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('datatime_order', sa.DateTime(), nullable=False),
    sa.Column('type_order', sa.Enum('in_hall', 'with_myself', name='typeorder'), nullable=True),
    sa.Column('status_order', sa.Enum('waiting_for_payment', 'paid', 'waiting_for_confirmation', 'confirmed', 'prepared', 'ready', 'waiting_for_the_courier', 'delivery', 'completed', name='statusorder'), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_order_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order')),
    sa.UniqueConstraint('trace_id', name=op.f('uq_order_trace_id'))
    )
    op.create_table('sweet_product_to_ingredient',
    sa.Column('id_sweet_product', sa.Integer(), nullable=False),
    sa.Column('id_ingredient', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_ingredient'], ['ingredient.id'], name=op.f('fk_sweet_product_to_ingredient_id_ingredient_ingredient')),
    sa.ForeignKeyConstraint(['id_sweet_product'], ['sweet_product.id'], name=op.f('fk_sweet_product_to_ingredient_id_sweet_product_sweet_product')),
    sa.PrimaryKeyConstraint('id_sweet_product', 'id_ingredient', name=op.f('pk_sweet_product_to_ingredient'))
    )
    op.create_table('order_to_sweet_product',
    sa.Column('id_order', sa.Integer(), nullable=False),
    sa.Column('id_sweet_product', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_order'], ['order.id'], name=op.f('fk_order_to_sweet_product_id_order_order')),
    sa.ForeignKeyConstraint(['id_sweet_product'], ['sweet_product.id'], name=op.f('fk_order_to_sweet_product_id_sweet_product_sweet_product')),
    sa.PrimaryKeyConstraint('id_order', 'id_sweet_product', name=op.f('pk_order_to_sweet_product'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_to_sweet_product')
    op.drop_table('sweet_product_to_ingredient')
    op.drop_table('order')
    op.drop_table('users')
    op.drop_table('sweet_product')
    op.drop_table('type')
    op.drop_table('role')
    op.drop_table('ingredient')
    op.drop_table('bakery')
    # ### end Alembic commands ###
