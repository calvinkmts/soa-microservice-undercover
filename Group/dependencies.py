from nameko.extensions import DependencyProvider

import pymysqlpool
import pymysql
import datetime

# ========================================================================================
# ----------------------------------- Database Wrapper -----------------------------------
# ========================================================================================

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
        sql = "SELECT * FROM `group` WHERE 1    "
        cursor.execute(sql)
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

    def get_group_by_id(self,id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM `group` WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def search_group(self,name):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM `group` WHERE `name` = %s"
        cursor.execute(sql,
                        (
                            name
                        )
                    )
        result = cursor.fetchone()
        cursor.close()
        return result

    def delete_group(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE FROM `group` WHERE `id` = %s"
        cursor.execute(sql,
                        (
                            id
                        )
                    )
        cursor.close()
        self.connection.commit()

    def get_all_schedule(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM group_schedule"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_group': row['id_group'],
                'id_user' : row['id_user'],
                'date': row['date'],
                'start_time': row['start_time'],
                'end_time': row['end_time']
            })
        cursor.close()
        return result

    def get_all_schedule_by_id_user(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM group_schedule WHERE id_user = {}".format(id)
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_group': row['id_group'],
                'id_user' : row['id_user'],
                'date': row['date'],
                'start_time': row['start_time'],
                'end_time': row['end_time']
            })
        cursor.close()
        return result

    def get_all_schedule_by_id_group(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM group_schedule WHERE id_group = {}".format(id)
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_group': row['id_group'],
                'id_user' : row['id_user'],
                'date': row['date'],
                'start_time': row['start_time'],
                'end_time': row['end_time']
            })
        cursor.close()
        return result
    
    def get_schedule_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM group_schedule WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def add_schedule(self, id_group, id_user, date, start_time):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO group_schedule VALUES(default, %s, %s, %s, %s, default)"
        cursor.execute( sql, 
                        (
                            id_group, 
                            id_user,
                            date,
                            start_time
                        )
                    )
        self.connection.commit()

    def edit_schedule_date(self, id, date):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE group_schedule SET date = %s WHERE id = %s"
        cursor.execute(sql,(date,id))
        self.connection.commit()
        
    def edit_schedule_start(self, id, start_time):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE group_schedule SET start_time = %s WHERE id = %s"
        cursor.execute(sql,(start_time,id))
        self.connection.commit()

    def edit_schedule_end(self, id, end_time):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE group_schedule SET end_time = %s WHERE id = %s"
        cursor.execute(sql,(end_time,id))
        self.connection.commit()

    def delete_schedule(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE FROM group_schedule WHERE id = {}".format(id)
        cursor.execute(sql)
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
        sql = "UPDATE `group_member` SET `status`= 0 WHERE 1 id = %s"
        cursor.execute(sql,
                        (
                            id
                        )
                    )
        cursor.close()
        self.connection.commit()
    
    def search_group_member(self, id_group):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM `group_member` WHERE `id_group` = {}".format(id_group)
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_group': row['id_group'],
                'id_user' : row['id_user']
            })
        cursor.close()
        return result


    def close_connection(self):
        self.connection.close()
        

# ========================================================================================
# --------------------------------- Dependency Provider ----------------------------------
# ========================================================================================

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        print("DB Dependency Constructor")
        config={'host':'localhost', 'user':'root', 'password':'', 'database':'proyeksoa', 'autocommit':True}
        self.connection_pool = pymysqlpool.ConnectionPool(size=5, name='DB Pool', **config)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def __del__(self):
        print("DB Dependency Destructor")
    
    



