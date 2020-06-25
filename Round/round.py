from nameko.rpc import rpc, RpcProxy

import dependencies
import schemas


class RoundService:
    name = 'round_service'
    database = dependencies.Database()
    user_rpc = RpcProxy('user_service')
    game_rpc = RpcProxy('game_service')

    def __init__(self):
        print("Service Constructor")

    ### GAME ROUND ###
    @rpc
    def create_round(self, id_game, round, word1, word2, num_mr_white, num_civilian, num_undercover):
        result = {
            'err': 0,
            'msg': 'Round Created'
        }
        self.database.create_round(id_game, round, word1, word2, num_mr_white, num_civilian, num_undercover)
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_round(self, id, round, num_mr_white, num_civilian, num_undercover):
        result = {
            'err': 0,
            'msg': 'Round Updated'
        }
        if self.database.get_round_by_id(id):
            self.database.update_round(id, round, num_mr_white, num_civilian, num_undercover)
        else:
            result['err'] = 1
            result['msg'] = 'Round Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_round(self, id):
        result = {
            'err': 0,
            'msg': 'Round Deleted'
        }
        if self.database.get_round_by_id(id):
            self.database.delete_round(id)
        else:
            result['err'] = 1
            result['msg'] = 'Round Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_round(self):
        result = self.database.get_all_round()
        return schemas.RoundSchema(many=True).dump(result)

    @rpc
    def get_round_by_id(self, id):
        result = self.database.get_round_by_id(id)
        return schemas.GameSchema().dump(result)

    ### ROUND DETAIL ###
    @rpc
    def create_round_detail(self, id_round, id_user, id_role, condition):
        result = {
            'err': 0,
            'msg': 'Round Detail Created'
        }
        if not self.game_rpc.get_round_by_id(id_round):
            result['err'] = 1
            result['msg'] = 'Round Not Found'
        elif not self.user_rpc.get_user_by_id(id_user):
            result['err'] = 1
            result['msg'] = 'User Not Found'
        else:
            self.database.create_round_detail(id_round, id_user, id_role, condition)
            self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_round_detail(self, id, id_user, condition):
        result = {
            'err': 0,
            'msg': 'Round Detail Updated'
        }
        if not self.database.get_round_detail_by_id(id):
            result['err'] = 1
            result['msg'] = 'Round Detail Not Found'
        elif not self.user_rpc.get_user_by_id(id_user):
            result['err'] = 1
            result['msg'] = 'User Not Found'
        else:
            self.database.update_round_detail(id, id_user, condition)
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_round_detail(self, id):
        result = {
            'err': 0,
            'msg': 'Round Detail Deleted'
        }
        if self.database.get_round_detail_by_id(id):
            self.database.delete_round_detail(id)
        else:
            result['err'] = 1
            result['msg'] = 'Round Detail Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_round_detail(self):
        result = self.database.get_all_round_detail()
        return schemas.RoundDetailSchema(many=True).dump(result)

    @rpc
    def get_round_detail_by_id(self, id):
        result = self.database.get_round_detail_by_id(id)
        return schemas.RoundDetailSchema().dump(result)

    ### TURN DETAIL ###
    @rpc
    def create_turn_detail(self, id_round_detail, turn, user_word, user_desc):
        result = {
            'err': 0,
            'msg': 'Turn Detail Created'
        }
        self.database.create_turn_detail(id_round_detail, turn, user_word, user_desc)
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_turn_detail(self, id, id_round_detail, turn, user_word, user_desc):
        result = {
            'err': 0,
            'msg': 'Turn Detail Updated'
        }
        if self.database.get_turn_detail_by_id(id):
            self.database.update_turn_detail(id)
        else:
            result['err'] = 1
            result['msg'] = 'Turn Detail Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_turn_detail(self, id):
        result = {
            'err': 0,
            'msg': 'Turn Detail Deleted'
        }
        if self.database.get_turn_detail_by_id(id):
            self.database.delete_turn_detail(id)
        else:
            result['err'] = 1
            result['msg'] = 'Turn Detail Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_turn_detail(self):
        result = self.database.get_all_turn_detail()
        return schemas.TurnDetailSchema(many=True).dump(result)

    @rpc
    def get_turn_detail_by_id(self, id):
        result = self.database.get_turn_detail_by_id(id)
        return schemas.TurnDetailSchema().dump(result)

    def __del__(self):
        print("Service Destructor")