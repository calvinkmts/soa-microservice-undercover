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

    @rpc
    def check_win(self, data):
        return 1

    @rpc
    def mrwhite_guess(self, data):
        win = self.database.mrwhite_guess(data)
        self.database.close_connection()
        if win:
            return "Mr. White's guess is right!"
        else:
            return "Try again next time!"

    ### GAME ROUND ###
    @rpc
    def create_round(self, data):
        result = {
            'err': 0,
            'msg': 'Round Created'
        }
        self.database.create_round(data)
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_round(self, data):
        result = {
            'err': 0,
            'msg': 'Round Updated'
        }
        if self.database.get_round_by_id(data['id']):
            self.database.update_round(data)
        else:
            result['err'] = 1
            result['msg'] = 'Round Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_round(self, data):
        result = {
            'err': 0,
            'msg': 'Round Deleted'
        }
        if self.database.get_round_by_id(data['id']):
            self.database.delete_round(data['id'])
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
        result = self.database.get_round_by_id(data['id'])
        return schemas.RoundSchema().dump(result)

    ### ROUND DETAIL ###
    @rpc
    def create_round_detail(self, data):
        result = {
            'err': 0,
            'msg': 'Round Detail Created'
        }
        if not self.game_rpc.get_round_by_id(data['id_round']):
            result['err'] = 1
            result['msg'] = 'Round Not Found'
        elif not self.user_rpc.get_user_by_id(data['id_user']):
            result['err'] = 1
            result['msg'] = 'User Not Found'
        else:
            self.database.create_round_detail(data)
            self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_round_detail(self, data):
        result = {
            'err': 0,
            'msg': 'Round Detail Updated'
        }
        if not self.database.get_round_detail_by_id(data['id']):
            result['err'] = 1
            result['msg'] = 'Round Detail Not Found'
        elif not self.user_rpc.get_user_by_id(data['id_user']):
            result['err'] = 1
            result['msg'] = 'User Not Found'
        else:
            self.database.update_round_detail(data)
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_round_detail(self, data):
        result = {
            'err': 0,
            'msg': 'Round Detail Deleted'
        }
        if self.database.get_round_detail_by_id(data['id']):
            self.database.delete_round_detail(data['id'])
        else:
            result['err'] = 1
            result['msg'] = 'Round Detail Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_round_detail(self):
        result = self.database.get_all_round_detail()
        return schemas.RoundDetailSchema(many=True).dump(result)

    @rpc
    def get_round_detail_by_id(self, data):
        result = self.database.get_round_detail_by_id(data['id'])
        return schemas.RoundDetailSchema().dump(result)

    ### TURN DETAIL ###
    @rpc
    def create_turn_detail(self, data):
        result = {
            'err': 0,
            'msg': 'Turn Detail Created'
        }
        self.database.create_turn_detail(data)
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_turn_detail(self, data):
        result = {
            'err': 0,
            'msg': 'Turn Detail Updated'
        }
        if self.database.get_turn_detail_by_id(data['id']):
            self.database.update_turn_detail(data['id'])
        else:
            result['err'] = 1
            result['msg'] = 'Turn Detail Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_turn_detail(self, data):
        result = {
            'err': 0,
            'msg': 'Turn Detail Deleted'
        }
        if self.database.get_turn_detail_by_id(data['id']):
            self.database.delete_turn_detail(data['id'])
        else:
            result['err'] = 1
            result['msg'] = 'Turn Detail Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_turn_detail(self):
        result = self.database.get_all_turn_detail()
        return schemas.TurnDetailSchema(many=True).dump(result)

    @rpc
    def get_turn_detail_by_id(self, data):
        result = self.database.get_turn_detail_by_id(data['id'])
        return schemas.TurnDetailSchema().dump(result)

    def __del__(self):
        print("Service Destructor")