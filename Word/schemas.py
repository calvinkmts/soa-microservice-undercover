from marshmallow import Schema, fields


class WordpackSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Int(required=True)
    status = fields.Str(required=True)
    created_at = fields.DateTime()
    last_update = fields.DateTime()

class WordpairSchema(Schema):
    id = fields.Int(required=True)
    id_word_pack = fields.Int(required=True)
    word_1 = fields.Str(required=True)
    word_2 = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.DateTime()
    last_update = fields.DateTime()

class CommandResultSchema(Schema):
    err = fields.Int(required=True)
    msg = fields.Str(required=True)
