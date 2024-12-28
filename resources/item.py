import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operations on items")

@blp.route('/item/<item_id>')
class Store(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Store not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")

    @blp.arguments(ItemUpdateSchema) # Here we decorate the method with the schema
    @blp.response(200, ItemSchema) # this is down 
    def put(self,item_data, item_id):
        
        try:
            item = items[item_id]
            item |= item_data # how to update a dictionary in python
            return item
        except KeyError:
            abort(404, message="Item not found.")


@blp.route('/item')
class Store(MethodView):
    @blp.arguments(ItemSchema) # Here we decorate the method with the schema
    @blp.response(201, ItemSchema) # this is down
    def post(self,item_data):

        item = ItemModel(**item_data) # how to create a dictionary in python

        try:
            db.session.add(item)
            db.session.commit()

        except SQLAlchemyError as e:
            db.session.rollback()
            abort(400, message="An error occurred while adding the item.")


        return  item
    
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()
