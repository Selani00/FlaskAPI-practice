from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = True, nullable = False)

    
    items = db.relationship('ItemModel', back_populates="store", lazy='dynamic')

    # lazy='dynamic' means that items is not fetch from the database until we tell to do so.

    