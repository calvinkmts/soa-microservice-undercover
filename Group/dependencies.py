from nameko.extensions import DependencyProvider

import pymysqlpool
import pymysql
from datetime import date
import datetime

# ========================================================================================
# ----------------------------------- Database Wrapper -----------------------------------
# ========================================================================================
# n.rpc.group_service.get_all_group()


class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Constructor")
        self.connection = connection

    def create_group(self, name):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO `group`(`id`, `name`, `status`) VALUES (default,%s,1)"
        cursor.execute(sql,
                       (
                           name
                       )
                       )
        self.connection.commit()

    def edit_group(self, id, name):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE `group` SET `name` = %s WHERE `id` = %s"
        cursor.execute(sql,
                       (
                           name,
                           id
                       )
                       )
        self.connection.commit()

    def get_all_group(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM `group` WHERE status = 1"
        cursor.execute(sql)
        if (cursor.rowcount != 0):
            for row in cursor.fetchall():
                result.append({
                    'id': row['id'],
                    'name': row['name'],
                    'status': row['status'],
                    'created_at': row['created_at'],
                    'last_update': row['last_update']
                })
        cursor.close()
        return result

    def get_group_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM `group` WHERE id = {}".format(id)
        cursor.execute(sql)
        if (cursor.rowcount != 0):
            row = cursor.fetchone()
            result.append({
                'id': row['id'],
                'name': row['name'],
                'status': row['status'],
                'created_at': row['created_at'],
                'last_update': row['last_update']
            })
        cursor.close()
        return result

    def get_group_by_name(self, name):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM `group` WHERE `status` = 1 AND `name` = %s"
        cursor.execute(sql,
                       (
                           name
                       )
                       )
        if (cursor.rowcount != 0):
            row = cursor.fetchone()
            result.append({
                'id': row['id'],
                'name': row['name'],
                'status': row['status'],
                'created_at': row['created_at'],
                'last_update': row['last_update']
            })
        cursor.close()
        return result

    def delete_group(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE `group` SET `status` = 0 WHERE `id` = %s"
        cursor.execute(sql,
                       (
                           id
                       )
                       )
        self.connection.commit()

    def get_all_schedule(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM group_schedule WHERE status = 1"
        cursor.execute(sql)
        if (cursor.rowcount != 0):
            for row in cursor.fetchall():
                result.append({
                    'id': row['id'],
                    'id_group': row['id_group'],
                    'id_user': row['id_user'],
                    'date': row['date'],
                    'start_time': row['start_time'],
                    'end_time': row['end_time']
                })
        cursor.close()
        return result

    def get_all_schedule_by_id_user(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM group_schedule WHERE status = 1 AND id_user = {}".format(id)
        cursor.execute(sql)
        if (cursor.rowcount != 0):
            for row in cursor.fetchall():
                result.append({
                    'id': row['id'],
                    'id_group': row['id_group'],
                    'id_user': row['id_user'],
                    'date': row['date'],
                    'start_time': row['start_time'],
                    'end_time': row['end_time']
                })
        cursor.close()
        return result

    def get_all_schedule_by_id_group(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM group_schedule WHERE status = 1 AND id_group = {}".format(id)
        cursor.execute(sql)
        if (cursor.rowcount != 0):
            for row in cursor.fetchall():
                result.append({
                    'id': row['id'],
                    'id_group': row['id_group'],
                    'id_user': row['id_user'],
                    'date': row['date'],
                    'start_time': row['start_time'],
                    'end_time': row['end_time']
                })
        cursor.close()
        return result

    def get_schedule_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM group_schedule WHERE id = {}".format(id)
        cursor.execute(sql)
        if (cursor.rowcount != 0):
            row = cursor.fetchone()
            result.append({
                'id': row['id'],
                'id_group': row['id_group'],
                'id_user': row['id_user'],
                'date': row['date'],
                'start_time': row['start_time'],
                'end_time': row['end_time']
            })
        cursor.close()
        return result

    def add_schedule(self, id_group, id_user, date, start_time, end_time):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO group_schedule VALUES(default, %s, %s, %s, %s, %s, '1')"
        cursor.execute(sql,
                       (
                           id_group,
                           id_user,
                           date,
                           start_time,
                           end_time
                       )
                       )
        self.connection.commit()

    def edit_schedule_date(self, id, date):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE group_schedule SET date = %s WHERE id = %s"
        cursor.execute(sql, (date, id))
        self.connection.commit()

    def edit_schedule_start(self, id, start_time):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE group_schedule SET start_time = %s WHERE id = %s"
        cursor.execute(sql, (start_time, id))
        self.connection.commit()

    def edit_schedule_end(self, id, end_time):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE group_schedule SET end_time = %s WHERE id = %s"
        cursor.execute(sql, (end_time, id))
        self.connection.commit()

    def delete_schedule(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE `group_member` SET `status`= 0 WHERE id = %s"
        cursor.execute(sql, (id))
        cursor.close()
        return "Record Deleted"

    def add_group_member(self, id_group, id_user):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO `group_member`(`id`, `id_group`, `id_user`, `status`) VALUES (default, %s, %s, 1)"
        cursor.execute(sql,
                       (
                           id_group,
                           id_user
                       )
                       )
        self.connection.commit()

    def remove_group_member(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE `group_member` SET `status`= 0 WHERE id = %s"
        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def search_group_member(self, id_group):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM `group_member` WHERE `status` = 1 AND `id_group` = {}".format(
            id_group)
        cursor.execute(sql)
        if (cursor.rowcount != 0):
            for row in cursor.fetchall():
                result.append({
                    'id': row['id'],
                    'id_group': row['id_group'],
                    'id_user': row['id_user']
                })
        cursor.close()
        return result

    def get_all_group_member(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM `group_member` WHERE `status` = 1"
        cursor.execute(sql)
        if (cursor.rowcount != 0):
            for row in cursor.fetchall():
                result.append({
                    'id': row['id'],
                    'id_group': row['id_group'],
                    'id_user': row['id_user']
                })
        cursor.close()
        return result

    def check_schedule(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        dateToday = date.today()
        sql = "SELECT * FROM `group_schedule` WHERE date = %s AND status = 1"
        cursor.execute(sql,
                       (
                           dateToday
                       )
                    )
        if (cursor.rowcount != 0):
            for row in cursor.fetchall():
                result.append({
                    'id': row['id'],
                    'id_group': row['id_group'],
                    'id_user': row['id_user'],
                    'date': row['date'],
                    'start_time': row['start_time']
                })
        cursor.close()
        return result

    def check_close_schedule_game(self, n_endtime, n_date):
        current_hour = datetime.datetime.now().hour
        current_min = datetime.datetime.now().minute
        menitNow = (int(current_hour) * 60) + (int(current_min))
        
        tanggal = str(n_date) + " " + str(n_endtime)
        waktu = datetime.datetime.strptime(tanggal, '%Y-%m-%d %H:%M:%S')
        menit = (int(waktu.hour) * 60) + (int(waktu.minute))        

        if(menitNow >= menit):
            return True
        else:
            return False

    def close_schedule_game(self, game_member):
        result = []
        member = 0
        for row in game_member:
            result.append({
                'status': row['status'],
                'id_member': row['id_member']
            })
        for i in result:
            if (i['status'] == "ACTIVE"):
                member = 1
        if (member > 0):
            return False
        else:
            return True


    def close_connection(self):
        self.connection.close()


# ========================================================================================
# --------------------------------- Dependency Provider ----------------------------------
# ========================================================================================

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        print("DB Dependency Constructor")
        config = {'host': '127.0.0.1', 'user': 'root',
                  'password': '', 'database': 'proyeksoa', 'autocommit': True}
        self.connection_pool = pymysqlpool.ConnectionPool(
            size=5, name='DB Pool', **config)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())

    def __del__(self):
        print("DB Dependency Destructor")
