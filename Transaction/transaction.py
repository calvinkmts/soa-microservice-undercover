from nameko.rpc import rpc,RpcProxy
from datetime import datetime
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
    word_rpc = RpcProxy('word_service')
    user_rpc = RpcProxy('user_service')
    transaction_rpc = RpcProxy('transaction_service')


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
        user = self.user_rpc.get_user_by_id(data['id_user'])
        if user:
            wordpack = self.word_rpc.get_wordpack_by_id(data['id_word_pack'])
            if wordpack:
                new_balance = user['balance'] - wordpack['price']
                if new_balance >= 0:
                    data['amount'] = wordpack['price']
                    self.database.create_transaction(data)
                    self.user_rpc.create_user_wordpack({'id_user': data['id_user'], 'id_word_pack': data['id_word_pack'], 'created_at': None, 'updated_at': None})
                    self.user_rpc.update_user({'id': user['id_user'], 'balance': new_balance})
                else:
                    result['err'] = 1
                    result['msg'] = 'Balance Not Enough'
            else:
                result['err'] = 1
                result['msg'] = 'Wordpack Not Found'
        else:
            result['err'] = 1
            result['msg'] = 'User Not Found'
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

    @rpc
    def delete_transaction(self, id):
        result = {
            'err': 0,
            'msg': 'Transaction Deleted'
        }

        if self.database.get_transaction_by_id(id):
            self.database.delete_transaction(id)
            
            self.database.close_connection()

        else:
            result['err'] = 1
            result['msg'] = 'Transaction Not Found'
            self.database.close_connection()

        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_voucher(self):
        voucher = self.database.get_all_voucher()
        self.database.close_connection()
        return schemas.VoucherSchema(many=True).dump(voucher)
    
    @rpc
    def get_voucher_by_id(self, id):
        voucher = self.database.get_voucher_by_id(id)
        self.database.close_connection()
        return schemas.VoucherSchema().dump(voucher)


    @rpc
    def search_voucher(self, code):
        voucher = self.database.search_voucher(code)
        self.database.close_connection()
        return voucher['status'] == 1, schemas.VoucherSchema().dump(voucher)
        print(voucher['status'])
    
    @rpc
    def create_voucher(self, data):

        result = {
            'err': 0,
            'msg': 'Voucher Created'
        }

        if self.database.search_voucher(data['code']):
            result['err'] = 1
            result['msg'] = 'Code Already Exists & Active'
        else:
            self.database.create_voucher(data)
            
            self.database.close_connection()
        
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_voucher(self, data):
        result = {
            'err': 0,
            'msg': 'Voucher Updated'
        }

        if self.database.get_voucher_by_id(data['id']):
            self.database.update_voucher(data)
            
            self.database.close_connection()

        else:
            result['err'] = 1
            result['msg'] = 'Voucher Not Found'
            self.database.close_connection()

        return schemas.CommandResultSchema().dumps(result)
        
    @rpc
    def delete_voucher(self, id):
        result = {
            'err': 0,
            'msg': 'Voucher Deleted'
        }

        if self.database.get_voucher_by_id(id):
            self.database.delete_voucher(id)
            
            self.database.close_connection()

        else:
            result['err'] = 1
            result['msg'] = 'Voucher Not Found'
            self.database.close_connection()

        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def redeem_voucher(self,data):
        
        result = {
            'err': 0,
            'msg': 'Voucher Redeemed'
        }


        if self.database.search_voucher(data['code']):
            if self.transaction_rpc.search_voucher(data['code']):
                # self.database.redeem_voucher(data)
                # result['msg'] = 'Redeem Successfully'
                # self.database.close_connection()
                if self.user_rpc.get_user_by_id(data['redeemed_by']): #cek user ada atau ga
                    tmp = self.user_rpc.get_user_by_id(data['redeemed_by'])
                    tmp1 = self.transaction_rpc.search_voucher(data['code'])

                    uawal = int(tmp['balance'])
                    topup = tmp1[1]['amount']
                    uakhir= uawal+topup
                    statusvoc = tmp1[0]
                    
                    if statusvoc:
                        self.user_rpc.update_user({"id": data['redeemed_by'],"balance": uakhir})
                        self.database.redeem_voucher(data)
                        now = datetime.now()
                        dt_string=now.strftime("%Y-%m-%d %H:%M:%S")
                        print(dt_string)
                        result['err'] = 0
                        result['msg'] = 'Voucher Redeemed by' + " " + tmp['name']
                    else:
                        result['err'] = 0
                        result['msg'] = 'Voucher Cant be Redeemed'

            
                    self.database.close_connection()
                else:
                    result['err'] = 1
                    result['msg'] = 'User tidak ada'
                    self.database.close_connection()
            else:
                result['err'] = 1
                result['msg'] = 'Code Already Inactive'
                self.database.close_connection()
        else:
            result['err'] = 1
            result['msg'] = 'Code Not Found'
            self.database.close_connection()

        
        return schemas.CommandResultSchema().dumps(result)

    def __del__(self):
        print("Service Destructor")
