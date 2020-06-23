from nameko.rpc import rpc,RpcProxy

import dependencies, schemas

class VoucherService:
    # ==========================================================
    # ---------------------- Service Name ----------------------
    # ==========================================================
    
    name = 'voucher_service'

    # ==========================================================
    # ----------------------- Dependency -----------------------
    # ==========================================================

    database = dependencies.Database()
    voucher_rpc = RpcProxy('voucher_service')

    # ==========================================================
    # -----------------------   Proxy   ------------------------
    # ==========================================================

    # voucher_rpc = RpcProxy('brewery_service')

    # ==========================================================
    # ------------------------ Functions -----------------------
    # ==========================================================

    def __init__(self):
        print("Service Constructor")

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
        return voucher['status'] == 1
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
    def delete_voucher(self, data):
        result = {
            'err': 0,
            'msg': 'Voucher Deleted'
        }

        if self.database.get_voucher_by_id(data['id']):
            self.database.delete_voucher(data)
            
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

        

        # if self.database.redeem_voucher(data):
        #     self.database.redeem_voucher(data['code'],data['redeemed_by'])
        
        # elif not self.database.redeem_voucher(data['code']):
        #     result['err'] = 1
        #     result['msg'] = 'Code Already Inactive'


        if self.database.search_voucher(data['code']):
            if self.voucher_rpc.search_voucher(data['code']):
                self.database.redeem_voucher(data)
                result['msg'] = 'Redeem Successfully'
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