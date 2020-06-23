from marshmallow import Schema, fields

class VoucherSchema(Schema):
    id = fields.Int(required=True)
    redeemed_by = fields.Int(required=False)
    code = fields.Str(required=True)
    amount = fields.Int(required=True)
    status = fields.Int(required=True) 

class CommandResultSchema(Schema):
    err = fields.Int(required=True)
    msg = fields.Str(required=True)