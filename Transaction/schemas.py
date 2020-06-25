from marshmallow import Schema, fields

class TransactionSchema(Schema):
    id = fields.Int(required=True)
    id_user = fields.Int(required=False)
    id_word_pack = fields.Int(required=True)
    amount = fields.Number(required=True)
    code = fields.Str(required=True)
    created_at = fields.Str()

class VoucherSchema(Schema):
    id = fields.Int(required=True)
    redeemed_by = fields.Int(required=False)
    code = fields.Str(required=True)
    amount = fields.Int(required=True)
    status = fields.Int(required=True) 
    

class CommandResultSchema(Schema):
    err = fields.Int(required=True)
    msg = fields.Str(required=True)