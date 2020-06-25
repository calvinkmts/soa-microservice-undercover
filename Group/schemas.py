from marshmallow import Schema, fields

class GroupSchema(Schema):
    id = fields.Int(required=True)
    id_group = fields.Int(required=True)
    id_user = fields.Int(required=True) 
    name = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    status = fields.Int(required=True)
    date = fields.Str(required=True)
    start_time = fields.Str(required=True)
    end_time =  fields.Str()
    id_gamemaster = fields.Int()
    id_schedule = fields.Int()

class ResultSchema(Schema):
    status = fields.Int(required=True)
    msg = fields.Str(required=True)
    data = fields.List(fields.Nested(GroupSchema))