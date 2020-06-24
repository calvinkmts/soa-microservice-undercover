from marshmallow import Schema, fields

class RoundSchema(Schema):
    id = fields.Int(required=True)
    id_game = fields.Int(required=True)
    round = fields.Int(required=True)
    word1 = fields.Str(required=True)
    word2 = fields.Str(required=True)
    num_mr_white = fields.Int(required=True)
    num_civilian = fields.Int(required=True)
    num_undercover = fields.Int(required=True)
    status = fields.Int(required=True)