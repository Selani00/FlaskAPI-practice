import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import db
from models import StoreModel
from sqlalchemy.exc import SQLAlchemyError,IntegrityError



from schemas import StoreSchema


blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route('/store/<store_id>')
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted successfully."}


@blp.route('/store')
class Store(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
    
    @blp.arguments(StoreSchema) # Here we decorate the method with the schema
    @blp.response(201, StoreSchema) # this is down
    def post(self,store_data):  

        store = StoreModel(**store_data) # how to create a dictionary in python

        try:
            db.session.add(store)
            db.session.commit()

        except IntegrityError:
            abort(400, message="A store with that name already exists.")

        except SQLAlchemyError as e:
            db.session.rollback()
            abort(400, message="An error occurred while adding the item.")


        return  store
    