from nameko.rpc import rpc, RpcProxy

import dependencies
import schemas


class GameService:
    name = 'game_service'
    database = dependencies.Database()
    user_rpc = RpcProxy('user_service')
    word_rpc = RpcProxy('word_service')

    def __init__(self):
        print("Service Constructor")

    ### GAME ###
    @rpc
    def create_game(self, data):
        result = {
            'err': 0,
            'msg': 'Game Created'
        }
        self.database.create_game(data)
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_game(self, data):
        result = {
            'err': 0,
            'msg': 'Game Updated'
        }
        if self.database.get_game_by_id(data['id']):
            self.database.update_game(data)
        else:
            result['err'] = 1
            result['msg'] = 'Game Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_game(self, data):
        result = {
            'err': 0,
            'msg': 'Game Deleted'
        }
        if self.database.get_game_by_id(data['id']):
            self.database.delete_game(data)
        else:
            result['err'] = 1
            result['msg'] = 'Game Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_game(self):
        result = self.database.get_all_game()
        return schemas.GameSchema(many=True).dump(result)

    @rpc
    def get_game_by_id(self, data):
        result = self.database.get_game_by_id(data['id'])
        return schemas.GameSchema().dump(result)
    
    @rpc
    def get_game_by_schedule_id(self, data):
        result = self.database.get_game_by_schedule_id(data['id'])
        return schemas.GameSchema().dump(result)
        
    ### GAME MEMBER ###
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
    
    ### GAME WORD PACK ###
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
