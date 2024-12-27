from marshmallow import Schema, fields
# This use to validate incoming data and outgoing data
# to add more validation rules, you can use the marshmallow library
class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True) # required=True means that the field is required in the request
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)