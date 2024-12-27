
from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint



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


# why use SQLAlchemy
# SQLAlchemy is a library that facilitates the communication between Python programs and databases.It's ORM(Object Relational Mapper) library that provides a way to interact with databases using Python objects. It is a high-level abstraction of the SQL database, which allows us to interact with the database without writing SQL queries.

