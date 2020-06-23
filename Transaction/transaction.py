from nameko.rpc import rpc,RpcProxy

import dependencies, schemas

class TransactionService:
    # ==========================================================
    # ---------------------- Service Name ----------------------
    # ==========================================================
    
    name = 'transaction_service'

    # ==========================================================
    # ----------------------- Dependency -----------------------
    # ==========================================================

    database = dependencies.Database()

    # ==========================================================
    # -----------------------   Proxy   ------------------------
    # ==========================================================

    # voucher_rpc = RpcProxy('voucher_service')
    # user_rpc = RpcProxy('user_service')
    # wordpack_rpc = RpcProxy('wordpack_service')

    # ==========================================================
    # ------------------------ Functions -----------------------
    # ==========================================================

    def __init__(self):
        print("Service Constructor")

    @rpc
    def get_all_transaction(self):
        transaction = self.database.get_all_transaction()
        self.database.close_connection()
        return schemas.TransactionSchema(many=True).dump(transaction)
    
    @rpc
    def get_transaction_by_id(self, id):
        transaction = self.database.get_transaction_by_id(id)
        self.database.close_connection()
        return schemas.TransactionSchema().dump(transaction)
    
    @rpc
    def create_transaction(self, data):

        result = {
            'err': 0,
            'msg': 'Transaction Created'
        }

        self.database.create_transaction(data)
        # update user balance
            # function
        # add user wordpack
            # function
            
        self.database.close_connection()
        
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_transaction(self, data):
        result = {
            'err': 0,
            'msg': 'Transaction Updated'
        }

        if self.database.get_transaction_by_id(data['id']):
            self.database.update_transaction(data)
            
            self.database.close_connection()

        else:
            result['err'] = 1
            result['msg'] = 'Transaction Not Found'
            self.database.close_connection()

        return schemas.CommandResultSchema().dumps(result)

    def __del__(self):
        print("Service Destructor")