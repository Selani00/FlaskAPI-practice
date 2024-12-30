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
        item = ItemModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted successfully."}

    @blp.arguments(ItemUpdateSchema) # Here we decorate the method with the schema
    @blp.response(200, ItemSchema) # this is down 
    def put(self,item_data, item_id):        
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id,**item_data)

        db.session.add(item)
        db.session.commit()

        return item
        


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
        return ItemModel.query.all()
