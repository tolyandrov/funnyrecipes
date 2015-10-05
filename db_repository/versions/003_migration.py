from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
recipe = Table('recipe', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
)

recipes = Table('recipes', post_meta,
    Column('recipe_id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=500)),
    Column('body', String(length=5000)),
)

users = Table('users', pre_meta,
    Column('user_id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=20)),
    Column('password', VARCHAR(length=10)),
    Column('email', VARCHAR(length=50)),
    Column('registered_on', DATETIME),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['recipe'].drop()
    post_meta.tables['recipes'].create()
    pre_meta.tables['users'].columns['registered_on'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['recipe'].create()
    post_meta.tables['recipes'].drop()
    pre_meta.tables['users'].columns['registered_on'].create()
