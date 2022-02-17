from db.session import db, metadata, engine

book = db.Table('book', metadata,
    db.Column('id', db.Integer(), primary_key=True, index=True),
    db.Column('title', db.String(255)),
    db.Column('subtitle', db.String(255)),
    db.Column('author', db.String(255))
)

metadata.create_all(engine)

