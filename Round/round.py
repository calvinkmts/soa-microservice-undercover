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
    def get_round_by_id(self, data):
        result = self.database.get_round_by_id(id)
        return schemas.GameSchema().dump(result)

    ### ROUND DETAIL ###
    @rpc
    def add_game_member(self, data):
        result = {
            'err': 0,
            'msg': 'Game Member Added'
        }
        if self.user_rpc.get_user_by_id(data['id_member']):
            self.database.add_game_member(data)
            self.database.close_connection()
        else:
            result['err'] = 1
            result['msg'] = 'User Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_game_member(self, data):
        result = {
            'err': 0,
            'msg': 'Game Member Updated'
        }
        if self.database.get_game_member_by_id(data['id']):
            self.database.update_game_member(data)
        else:
            result['err'] = 1
            result['msg'] = 'Game Member Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_game_member(self, data):
        result = {
            'err': 0,
            'msg': 'Game Member Deleted'
        }
        if self.database.get_game_member_by_id(data['id']):
            self.database.delete_game_member(data)
        else:
            result['err'] = 1
            result['msg'] = 'Game Member Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_game_member(self):
        result = self.database.get_all_game_member()
        return schemas.GameMemberSchema(many=True).dump(result)

    @rpc
    def get_game_member_by_id(self, data):
        result = self.database.get_game_by_id(data['id'])
        return schemas.GameMemberSchema().dump(result)

    @rpc
    def get_game_member_by_game_id(self, data):
        result = self.database.get_game_member_by_game_id(data['id'])
        return schemas.GameMemberSchema(many=True).dump(result)

    ### TURN DETAIL ###
    @rpc
    def create_game_wordpack(self, data):
        result = {
            'err': 0,
            'msg': 'Game Wordpack Added'
        }
        self.database.create_game_wordpack(data)
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_game_wordpack(self, data):
        result = {
            'err': 0,
            'msg': 'Game Wordpack Updated'
        }
        if self.database.get_game_wordpack_by_id(data['id']):
            self.database.update_game_wordpack(data)
        else:
            result['err'] = 1
            result['msg'] = 'Game Wordpack Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_game_wordpack(self, data):
        result = {
            'err': 0,
            'msg': 'Game Wordpack Deleted'
        }
        if self.database.get_game_wordpack_by_id(data['id']):
            self.database.delete_game_wordpack(data)
        else:
            result['err'] = 1
            result['msg'] = 'Game Wordpack Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_game_wordpack(self):
        result = self.database.get_all_game_wordpack()
        return schemas.GameWordpackSchema(many=True).dump(result)

    @rpc
    def get_game_wordpack_by_id(self, data):
        result = self.database.get_game_wordpack_by_id(data['id'])
        return schemas.GameWordpackSchema().dump(result)

    @rpc
    def get_game_wordpack_by_game_id(self, data):
        result = self.database.get_game_wordpack_by_game_id(data['id'])
        return schemas.GameWordpackSchema(many=True).dump(result)

    def __del__(self):
        print("Service Destructor")