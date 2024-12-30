from db import db

class TagModel(db.Model):
    __tablename__ = 'tags'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = False, nullable = False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"),nullable = False)

    
    tags = db.relationship('TagModel', back_populates="tags",lazy='dynamic', cascade="all, delete, delete-orphan")
    items = db.relationship('ItemModel', back_populates="tags", secondary="items_tags", lazy='dynamic')
    # lazy='dynamic' means that items is not fetch from the database until we tell to do so.

    