from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
import sqlalchemy as db


engine = db.create_engine('sqlite:///test.sqlite')
connection = engine.connect()

metadata = db.MetaData()


