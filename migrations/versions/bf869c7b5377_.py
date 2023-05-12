"""empty message

Revision ID: bf869c7b5377
Revises: 
Create Date: 2023-05-09 22:54:06.162416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf869c7b5377'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('barbers',
    sa.Column('barberid', sa.Integer(), nullable=False),
    sa.Column('barbername', sa.String(length=30), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('phonenumber', sa.String(length=13), nullable=True),
    sa.Column('forte', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('image', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('barberid')
    )
    op.create_table('blogs',
    sa.Column('blogid', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('subtitle', sa.String(length=80), nullable=True),
    sa.Column('content', sa.String(length=1000), nullable=True),
    sa.Column('postdate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('blogid'),
    sa.UniqueConstraint('subtitle'),
    sa.UniqueConstraint('title')
    )
    op.create_table('customers',
    sa.Column('customerid', sa.Integer(), nullable=False),
    sa.Column('customername', sa.String(length=60), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('phonenumber', sa.String(length=13), nullable=True),
    sa.Column('account', sa.String(length=60), nullable=True),
    sa.Column('isadmin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('customerid'),
    sa.UniqueConstraint('account')
    )
    op.create_table('services',
    sa.Column('serviceid', sa.Integer(), nullable=False),
    sa.Column('servicename', sa.String(length=50), nullable=True),
    sa.Column('timeofservice', sa.Integer(), nullable=True),
    sa.Column('price', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('serviceid'),
    sa.UniqueConstraint('servicename')
    )
    op.create_table('bookings',
    sa.Column('bookingid', sa.Integer(), nullable=False),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.Column('barberid', sa.Integer(), nullable=True),
    sa.Column('bookingtime', sa.DateTime(), nullable=True),
    sa.Column('state', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['barberid'], ['barbers.barberid'], ),
    sa.ForeignKeyConstraint(['customerid'], ['customers.customerid'], ),
    sa.PrimaryKeyConstraint('bookingid')
    )
    op.create_table('customerimages',
    sa.Column('cusimageid', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('barberid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['barberid'], ['barbers.barberid'], ),
    sa.PrimaryKeyConstraint('cusimageid')
    )
    op.create_table('worktime',
    sa.Column('worktimeid', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('timefrom', sa.Time(), nullable=True),
    sa.Column('timeto', sa.Time(), nullable=True),
    sa.Column('statework', sa.String(length=30), nullable=True),
    sa.Column('barberid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['barberid'], ['barbers.barberid'], ),
    sa.PrimaryKeyConstraint('worktimeid')
    )
    op.create_table('service_booking',
    sa.Column('bookingid', sa.Integer(), nullable=True),
    sa.Column('serviceid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bookingid'], ['bookings.bookingid'], ),
    sa.ForeignKeyConstraint(['serviceid'], ['services.serviceid'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service_booking')
    op.drop_table('worktime')
    op.drop_table('customerimages')
    op.drop_table('bookings')
    op.drop_table('services')
    op.drop_table('customers')
    op.drop_table('blogs')
    op.drop_table('barbers')
    # ### end Alembic commands ###
