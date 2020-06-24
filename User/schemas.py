from marshmallow import Schema, fields

class UsersSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    gender = fields.Str(required=True)
    dob = fields.Date(required=True)
    status = fields.Str(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    balance = fields.Int()

class UserWordPacksSchema(Schema):
    id = fields.Int(required=True)
    id_user = fields.Int(required=True)
    id_word_pack = fields.Int(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class CommandResultSchema(Schema):
    err = fields.Int(required=True)
    msg = fields.Str(required=True)