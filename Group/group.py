from nameko.rpc import rpc, RpcProxy

import dependencies, schemas
import json
import datetime

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
            'msg': 'Group Created'
        }

        self.database.create_group(name)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def edit_group(self, id, name):
        result = {
            'status': 0,
            'msg': 'Group Updated'
        }

        self.database.edit_group(id, name)
        return schemas.ResultSchema().dumps(result)
    
    @rpc
    def delete_group(self, id):
        result = {
            'status': 0,
            'msg': 'Group Deleted'
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
    def get_group_by_name(self,name):
        result = {
            'status': 0,
            'msg': ''
        }

        result['data'] = self.database.get_group_by_name(name)
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
    def add_schedule(self, id_group, id_user, date, start_time, end_time):
        result = {
            'status': 0,
            'msg': 'Schedule Created'
        }

        self.database.add_schedule(id_group, id_user, date, start_time)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def edit_schedule_date(self, id, date):
        result = {
            'status': 0,
            'msg': 'Schedule Updated'
        }

        self.database.edit_schedule_date(id,date)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def edit_schedule_start(self, id, start_time):
        result = {
            'status': 0,
            'msg': 'Schedule Updated'
        }

        self.database.edit_schedule_start(id, start_time)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def edit_schedule_end(self, id, end_time):
        result = {
            'status': 0,
            'msg': 'Schedule Updated'
        }

        self.database.edit_schedule_end(id, end_time)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def delete_schedule(self, id):
        result = {
            'status': 0,
            'msg': 'Schedule Deleted'
        }

        self.database.delete_schedule(id)
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)

    @rpc
    def add_group_member(self, id_group, id_user):
        result = {
            'status': 0,
            'msg': 'Group Member Added'
        }

        self.database.add_group_member(id_group, id_user)
        return schemas.ResultSchema().dumps(result)

    @rpc
    def remove_group_member(self, id):
        result = {
            'status': 0,
            'msg': 'Group Member Removed'
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

    @rpc
    def get_all_group_member(self):
        result = {
            'status': 0,
            'msg': ''
        }

        result['data'] = self.database.get_all_group_member()
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)

    @rpc
    def check_schedule(self):
        result = {
            'status': 0,
            'msg': '',
            'data': []
        }

        current_hour = datetime.datetime.now().hour
        current_min = datetime.datetime.now().minute
        menitNow = (int(current_hour) * 60) + (int(current_min))
        hasil = self.database.check_schedule()
        count = -1
        if (len(hasil) != 0):
            for i in hasil:
                tanggal = str(i['date']) + " " + str(i['start_time'])
                waktu = datetime.datetime.strptime(tanggal, '%Y-%m-%d %H:%M:%S')
                menit = (int(waktu.hour) * 60) + (int(waktu.minute))
                # print('now : ' + str(menitNow))
                # print(menit)
                if (menitNow == menit):
                    result['msg'] = 'Room Created'
                    count = count + 1
                    result['data'].append({
                        'id_schedule': i['id'],
                        'id_gamemaster' : i['id_user']
                    })
                    self.game_rpc.create_game(result['data'][count])

        self.database.close_connection()
        if(count == -1):
            result['msg'] = 'No Room Created'
        return schemas.ResultSchema().dumps(result)

    @rpc
    def close_schedule_game(self):
        result = {
            'status': 0,
            'msg': 'No Room Deleted'
        }

        hasilSchedule = []
        count = -1

        schedule = self.database.get_all_schedule()
        for i in schedule:
            hasilSchedule.append({
                'id': i['id']
            })
            count = count + 1
            id_game = self.game_rpc.get_game_by_schedule_id(hasilSchedule[count])
            
            if(self.database.check_close_schedule_game(i['end_time'], i['date']) == True):
                
                if('id' in id_game):
                    kirimanGameId = []
                    kirimanGameId.append({
                        'id': id_game['id']
                    })
                    
                    game_member = self.game_rpc.get_game_member_by_game_id(kirimanGameId[0])
                    
                    if (self.database.close_schedule_game(game_member) == True):
                        self.game_rpc.delete_game(kirimanGameId[0])
                        result['msg'] = 'Room Deleted'
        
        self.database.close_connection()
        return schemas.ResultSchema().dumps(result)

    def __del__(self):
        print("Service Destructor")