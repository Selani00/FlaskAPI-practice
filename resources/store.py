import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import stores

from schemas import StoreSchema


blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route('/store/<store_id>')
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found.")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")


@blp.route('/store')
class Store(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()
    
    @blp.arguments(StoreSchema) # Here we decorate the method with the schema
    @blp.response(201, StoreSchema) # this is down
    def post(self,store_data):  

        for store in stores.values():
            if store["name"] == store_data["name"]:
                abort(400, message="A store with the same name already exists.")
        store_id  = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store