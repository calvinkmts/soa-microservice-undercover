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

class RoundDetailSchema(Schema):
    id = fields.Int(required=True)
    id_round = fields.Int(required=True)
    id_user = fields.Int(required=True)
    id_role = fields.Int(required=True)
    condition = fields.Str(required=True)
    status = fields.Int(required=True)

class TurnDetailSchema(Schema):
    id = fields.Int(required=True)
    id_round_detail = fields.Int(required=True)
    turn = fields.Int(required=True)
    user_word = fields.Str(required=True)
    user_desc = fields.Str(required=True)
    status = fields.Int(required=True)

class ResultRoundSchema(Schema):
    status = fields.Int(required=True)
    msg = fields.Str(required=True)
    data = fields.List(fields.Nested(RoundSchema))

class ResultRoundDetailSchema(Schema):
    status = fields.Int(required=True)
    msg = fields.Str(required=True)
    data = fields.List(fields.Nested(RoundDetailSchema))

class ResultTurnDetailSchema(Schema):
    status = fields.Int(required=True)
    msg = fields.Str(required=True)
    data = fields.List(fields.Nested(TurnDetailSchema))