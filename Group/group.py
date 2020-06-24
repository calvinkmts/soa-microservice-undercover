from nameko.rpc import rpc

import dependencies, schemas
import json

class GroupService:
    # ==========================================================
    # ---------------------- Service Name ----------------------
    # ==========================================================
    
    name = 'group_service'

    # ==========================================================
    # ----------------------- Dependency -----------------------
    # ==========================================================

    database = dependencies.Database()

    # ==========================================================
    # -------------------------- Proxy -------------------------
    # ==========================================================

    game_rpc = RpcProxy('game_service')
    user_rpc = RpcProxy('user_service')

    # ==========================================================
    # ------------------------ Functions -----------------------
    # ==========================================================

    def __init__(self):
        print("Service Constructor")

    @rpc
    def create_group(self, name):
        result = {
            'status': 0,
            'msg': ''
        }

        self.database.create_group(name)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def edit_group(self, id, name):
        result = {
            'status': 0,
            'msg': ''
        }

        self.database.edit_group(id, name)
        return schemas.ResultSchema().dumps(result)
    
    @rpc
    def delete_group(self, id):
        result = {
            'status': 0,
            'msg': ''
        }

        self.database.delete_group(id)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def get_all_group(self):
        result = {
            'status': 0,
            'msg': ''
        }

        result['data'] = self.database.get_all_group()
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)

    @rpc
    def get_group_by_id(self,id):
        result = {
            'status': 0,
            'msg': ''           
        }

        result['data'] = self.database.get_group_by_id(id)
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)

    @rpc
    def search_group(self,name):
        result = {
            'status': 0,
            'msg': ''
        }

        result['data'] = self.database.search_group(name)
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)

    @rpc
    def get_all_schedule(self):
        result = {
            'status': 0,
            'msg': ''
        }

        result['data'] = self.database.get_all_schedule()
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)
    
    @rpc
    def get_schedule_by_id(self, id):
        result = {
            'status': 0,
            'msg': ''
        }

        result['data'] = self.database.get_schedule_by_id(id)
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)

    @rpc
    def get_schedule_by_id_user(self, id):
        result = {
            'status': 0,
            'msg': ''
        }

        result['data'] = self.database.get_all_schedule_by_id_user(id)
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)
    
    @rpc
    def get_schedule_by_id_group(self, id):
        result = {
            'status': 0,
            'msg': ''
        }

        result['data'] = self.database.get_all_schedule_by_id_group(id)
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)

    @rpc
    def add_schedule(self, id_group, id_user, date, start_time):
        result = {
            'status': 0,
            'msg': ''
        }

        self.database.add_schedule(id_group, id_user, date, start_time)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def edit_schedule_date(self, id, date):
        result = {
            'status': 0,
            'msg': ''
        }

        self.database.edit_schedule_date(id,date)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def edit_schedule_start(self, id, start_time):
        result = {
            'status': 0,
            'msg': ''
        }

        self.database.edit_schedule_start(id, start_time)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def edit_schedule_end(self, id, end_time):
        result = {
            'status': 0,
            'msg': ''
        }

        self.database.edit_schedule_end(id, end_time)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def delete_schedule(self, id):
        result = {
            'status': 0,
            'msg': ''
        }

        self.database.delete_schedule(id)
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)

    @rpc
    def add_group_member(self, id_group, id_user):
        result = {
            'status': 0,
            'msg': ''
        }

        self.database.add_group_member(id_group, id_user)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def remove_group_member(self, id):
        result = {
            'status': 0,
            'msg': ''
        }

        self.database.remove_group_member(id)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def search_group_member(self, id_group):
        result = {
            'status': 0,
            'msg': ''
        }

        result['data'] = self.database.search_group_member(id_group)
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)

    def __del__(self):
        print("Service Destructor")