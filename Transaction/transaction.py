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
    wordpack_rpc = RpcProxy('word_pack')
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
        
        
        # update user balance
            # function
        final = 0
        tmp = self.wordpack_rpc.get_wordPack_by_id(data['id_word_pack'])
        tmp1 = self.user_rpc.get_user_by_id(data['id_user'])
        saldo = 0
        harga = 0
        end = saldo - harga
        if self.user_rpc.get_user_by_id(data['id_user']): #cek ada ga usernya
            if self.wordpack_rpc.get_wordPack_by_id(data['id_word_pack']): #cek ada ga wordpacknya
                cek = self.wordpack_rpc.get_wordPack_by_id(data['id_word_pack'])
                he = cek['status']
                if he == 'ACTIVE':
                    tmp = self.wordpack_rpc.get_wordPack_by_id(data['id_word_pack'])
                    harga = tmp['price']

                    tmp1 = self.user_rpc.get_user_by_id(data['id_user'])
                    saldo = tmp1['balance']

                    if saldo >= harga:
                        
                        print(harga)
                        final = 1
                        # self.database.close_connection()

                        uakhir = saldo - harga
                        self.user_rpc.update_user({"id": data['id_user'],"balance": uakhir})

                        result['err'] = 0
                        result['msg'] = "Transaction Created"
                        self.database.close_connection()

                    else:
                        
                        result['err'] = 1
                        result['msg'] = 'Balance Not Enough'
                        self.database.close_connection()
                else:
                    result['err'] = 1
                    result['msg'] = 'Wordpack Not Active'
                    self.database.close_connection()
            else:
                result['err'] = 1
                result['msg'] = 'Wordpack Not Found'
                self.database.close_connection()
        else:
            result['err'] = 1
            result['msg'] = 'User Not Found'
            self.database.close_connection()


        # self.database.create_transaction({"id_user": data['id_user'], "id_word_pack": data['id_word_pack'], "type": 'PURCHASED', "amount": tmp['price'], "code": 'None', "created_at": dt_string,"updated_at": dt_string })
       # self.database.create_transaction(data)

        # add user wordpack
            # function
        
        if final==1:
            self.database.create_transaction({"id_user": data['id_user'], "id_word_pack": data['id_word_pack'],"amount": tmp['price']})

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
            'msg': ''
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