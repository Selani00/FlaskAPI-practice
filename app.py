import uuid
from flask import Flask,request
from flask_smorest import Api
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

import uuid


app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['API_TITLE'] = "Stores REST API"
app.config['API_VERSION'] = "v1"
app.config['OPENAPI_VERSION'] = "3.0.3"
app.config['OPENAPI_URL_PREFIX'] = "/"
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api=Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)

# @app.get("/store")
# def get_stores():
#     return {"stores": list(stores.values())}


# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     if "name" not in store_data:
#         abort(400, message="Invalid store data.")

#     for store in stores.values():
#         if store["name"] == store_data["name"]:
#             abort(400, message="A store with the same name already exists.")
#     store_id  = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store, 201


# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         abort(404, message="Store not found.")

# @app.delete("/store/<string:store_id>")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message": "Store deleted."}
#     except KeyError:
#         abort(404, message="Store not found.")


# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     if(
#         "name" not in item_data or
#         "price" not in item_data or
#         "store_id" not in item_data
#     ):
#         abort(400, message="Invalid item data."
#     )

#     for item in items.values():
#         if item["name"] == item_data["name"] and item["store_id"] == item_data["store_id"]:
#             abort(400, message="An item with the same name already exists.")

#     if item_data["store_id"] not in stores:
#         abort(404, message="Store not found.")
    
#     item_id  = uuid.uuid4().hex
#     item = {**item_data, "id": item_id}
#     items[item_id] = item

#     return  item, 201




# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}



# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, description="Item not found.")


# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item deleted."}
#     except KeyError:
#         abort(404, message="Item not found.")

# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#     if "name" not in item_data or "price" not in item_data:
#         abort(400, message="Invalid item data.")
#     try:
#         item = items[item_id]
#         item |= item_data # how to update a dictionary in python
#         return item
#     except KeyError:
#         abort(404, message="Item not found.")
    

