from nameko.rpc import rpc, RpcProxy

import dependencies, schemas

class UserService:
    name = 'user_service'
    database = dependencies.Database()
    # voucher_rpc = RpcProxy('voucher_service')
    # user_rpc = RpcProxy('user_service')
    # transaction_rpc = RpcProxy('transaction_service')

    def __init__(self):
        print("Service Constructor")

    @rpc
    def create_user(self, data):
        self.database.create_user(data)
        self.database.close_connection()
        return "New User Created"

    @rpc
    def update_user(self, data):

        result = {
            'err': 0,
            'msg': 'User Updated'
        }

        if self.database.get_user_by_id(data['id']):
            self.database.update_user(data)
            
            self.database.close_connection()

        else:
            result['err'] = 1
            result['msg'] = 'User Not Found'
            self.database.close_connection()

        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_user(self):
        user = self.database.get_all_user()
        self.database.close_connection()
        return schemas.UsersSchema(many=True).dump(user)

    @rpc
    def get_user_by_id(self, id):
        user = self.database.get_user_by_id(id)
        self.database.close_connection()
        return schemas.UsersSchema().dump(user)

    @rpc
    def set_user_active(self, id):
        self.database.set_user_active(id)
        return "Set Active Successfully"
    
    @rpc
    def create_user_wordpack(self, data):
        self.database.create_user_wordpack(data)
        self.database.close_connection()
        return "New User Wordpack Created"

    @rpc
    def update_user_wordpack(self, data):
        
        result = {
            'err': 0,
            'msg': 'User Wordpack Updated'
        }

        if self.database.get_user_wordpack_by_id(data['id']):
            self.database.update_user_wordpack(data)
            
            self.database.close_connection()

        else:
            result['err'] = 1
            result['msg'] = 'User Wordpack Not Found'
            self.database.close_connection()

        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_user_wordpack(self):
        wordpack = self.database.get_all_user_wordpack()
        self.database.close_connection()
        return schemas.UserWordPacksSchema(many=True).dump(wordpack)
    
    @rpc
    def get_user_wordpack_by_id(self, id):
        wordpack = self.database.get_user_wordpack_by_id(id)
        self.database.close_connection()
        return schemas.UserWordPacksSchema().dump(wordpack)

    @rpc
    def get_all_user_wordpack_by_user_id(self, id):
        wordpack = self.database.get_all_user_wordpack_by_user_id(id)
        self.database.close_connection()
        return schemas.UserWordPacksSchema(many=True).dump(wordpack)
    
    def __del__(self):
        print("Service Destructor")