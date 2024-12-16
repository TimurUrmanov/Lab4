from marshmallow import Schema, fields

class StoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    items = fields.List(fields.Nested("ItemSchema"), dump_only=True)