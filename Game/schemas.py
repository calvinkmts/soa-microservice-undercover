from marshmallow import Schema, fields


class GameSchema(Schema):
    id = fields.Int(required=True)
    status = fields.Str(required=True)
    id_gamemaster = fields.Int()
    id_schedule = fields.Int()
    created_at = fields.DateTime()

class GameMemberSchema(Schema):
    id = fields.Int(required=True)
    id_game = fields.Int(required=True)
    id_member = fields.Int(required=True)
    status = fields.Str(required=True)

class GameWordpackSchema(Schema):
    id = fields.Int(required=True)
    id_game = fields.Int(required=True)
    id_word_pack = fields.Int(required=True)
    id_contributor = fields.Int(required=True)

class CommandResultSchema(Schema):
    err = fields.Int(required=True)
    msg = fields.Str(required=True)
