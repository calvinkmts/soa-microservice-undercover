from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling


class DatabaseWrapper:
    connection = None

    def __init__(self, connection):
        self.connection = connection

    ### GAME ###
    def create_game(self, data):
        if('created_at' not in data):
            data['created_at'] = None
        if('id_gamemaster' not in data):
            data['id_gamemaster'] = None
        if('id_schedule' not in data):
            data['id_schedule'] = None
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO game VALUES(default, %s, 'ACTIVE', %s, %s)"
        cursor.execute(sql, (data['created_at'], data['id_gamemaster'], data['id_schedule']))
        cursor.close()
        self.connection.commit()

    def update_game(self, data):
        cursor = self.connection.cursor(dictionary=True)
        first = 1
        sql = "UPDATE game SET "
        if('status' in data):
            if(not first):
                sql += ","
            else:
                first = 0
            sql += "status = " + str(data['status'])
        if('id_gamemaster' in data):
            if(not first):
                sql += ","
            else:
                first = 0
            sql += "id_gamemaster = " + str(data['id_gamemaster'])
        sql += " WHERE id = " + str(data['id'])
        if(not first):
            cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def delete_game(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "DELETE FROM game WHERE id = {}".format((data['id']))
        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def get_all_game(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM game"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'created_at': row['created_at'],
                'status': row['status'],
                'id_gamemaster': row['id_gamemaster'],
                'id_schedule': row['id_schedule']
            })
        cursor.close()
        return result

    def get_game_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM game WHERE id = {}".format((id))
        cursor.execute(sql, id)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_game_by_schedule_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM game WHERE id_schedule = {}".format((id))
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    ### GAME MEMBER ###
    def add_game_member(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO game_member VALUES(default, %s, %s, 'WAITING')"
        cursor.execute(sql, (data['id_game'], data['id_member']))
        cursor.close()
        self.connection.commit()

    def update_game_member(self, data):
        cursor = self.connection.cursor(dictionary=True)
        first = 1
        sql = "UPDATE game_member SET "
        if('status' in data):
            if(not first):
                sql += ","
            else:
                first = 0
            sql += "status = " + str(data['status'])
        sql += " WHERE id = " + str(data['id'])
        if(not first):
            cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def delete_game_member(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "DELETE FROM game_member WHERE id = {}".format((data['id']))
        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def get_all_game_member(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM game_member"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_game': row['id_game'],
                'id_member': row['id_member'],
                'status': row['status']
            })
        cursor.close()
        return result
        
    def get_game_member_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM game_member WHERE id = {}".format((id))
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_game_member_by_game_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM game_member WHERE id_game = {}".format((id))
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_game': row['id_game'],
                'id_member': row['id_member'],
                'status': row['status']
            })
        cursor.close()
        return result

    ### GAME WORDPACK ###
    def create_game_wordpack(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO game_wordpack VALUES(default, %s, %s, %s)"
        cursor.execute(
            sql, (data['id_game'], data['id_word_pack'], data['id_contributor']))
        cursor.close()
        self.connection.commit()
    
    def update_game_wordpack(self, data):
        cursor = self.connection.cursor(dictionary=True)
        first = 1
        sql = "UPDATE game_wordpack SET "
        if('id_contributor' in data):
            if(not first):
                sql += ","
            else:
                first = 0
            sql += "id_contributor = " + str(data['id_contributor'])
        sql += " WHERE id = " + str(data['id'])
        if(not first):
            cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def delete_game_wordpack(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "DELETE FROM game_wordpack WHERE id = {}".format((data['id']))
        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def get_all_game_wordpack(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM game_wordpack"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_game': row['id_game'],
                'id_word_pack': row['id_word_pack'],
                'id_contributor': row['id_contributor']
            })
        cursor.close()
        return result

    def get_game_wordpack_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM game_wordpack WHERE id = {}".format((id))
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_game_wordpack_by_game_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM game_wordpack WHERE id_game = {}".format((id))
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_game': row['id_game'],
                'id_word_pack': row['id_word_pack'],
                'id_contributor': row['id_contributor']
            })
        cursor.close()
        return result

    def close_connection(self):
        self.connection.close()

    def __del__(self):
        self.close_connection()

class Database(DependencyProvider):
    connection_pool = None

    def __init__(self):
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="database_pool",
                pool_size=10,
                pool_reset_session=True,
                host='127.0.0.1',
                database='proyeksoa',
                user='root',
                password=''
            )
        except Error as e:
            print("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
