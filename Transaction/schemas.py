from marshmallow import Schema, fields

class TransactionSchema(Schema):
    id = fields.Int(required=True)
    id_user = fields.Int(required=False)
    id_word_pack = fields.Int(required=True)
    type = fields.Str(required=True)
    amount = fields.Number(required=True)
    code = fields.Str(required=True)
    status = fields.Str(required=True) 
    created_at = fields.DateTime(required=True,format='%Y-%m-%d %H:%M:%S')
    updated_at = fields.DateTime(required=True,format='%Y-%m-%d %H:%M:%S')
    

class CommandResultSchema(Schema):
    err = fields.Int(required=True)
    msg = fields.Str(required=True)