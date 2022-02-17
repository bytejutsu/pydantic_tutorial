from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
import sqlalchemy as db

engine = db.create_engine('sqlite:///test.sqlite')
connection = engine.connect()

metadata = db.MetaData()

book = db.Table('book', metadata,
    db.Column('id', db.Integer(), primary_key=True, index=True),
    db.Column('title', db.String(255)),
    db.Column('subtitle', db.String(255)),
    db.Column('author', db.String(255))
)

metadata.create_all(engine)