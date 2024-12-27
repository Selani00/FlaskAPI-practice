import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import items

blp = Blueprint("Items", __name__, description="Operations on items")

@blp.route('/items/<item_id>')
class Store(MethodView):
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


    def put(self, item_id):
        item_data = request.get_json()
        if "name" not in item_data or "price" not in item_data:
            abort(400, message="Invalid item data.")
        try:
            item = items[item_id]
            item |= item_data # how to update a dictionary in python
            return item
        except KeyError:
            abort(404, message="Item not found.")