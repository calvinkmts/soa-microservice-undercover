from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

import random

class DatabaseWrapper:
    connection = None

    def __init__(self, connection):
        self.connection = connection

    ### WORDPACK ###
    def create_wordpack(self, data):
        if('description' not in data):
            data['description'] = ''
        if('created_at' not in data):
            data['created_at'] = None
        if('last_update' not in data):
            data['last_update'] = None
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO wordpack VALUES(default, %s, %s, %s, 'ACTIVE', %s, %s)"
        cursor.execute(sql, (data['name'], data['description'], data['price'], data['created_at'], data['last_update']))
        cursor.close()
        self.connection.commit()

    def update_wordpack(self, data):
        cursor = self.connection.cursor(dictionary=True)
        first = 1
        sql = "UPDATE wordpack SET "
        if('name' in data):
            if(not first):
                sql += ","
            else:
                first = 0
            sql += "name = " + str(data['name'])
        if('description' in data):
            if(not first):
                sql += ","
            else:
                first = 0
            sql += "description = " + str(data['description'])
        if('price' in data):
            if(not first):
                sql += ","
            else:
                first = 0
            sql += "price = " + str(data['price'])
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

    def delete_wordpack(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "DELETE FROM wordpack WHERE id = {}".format((data['id']))
        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def get_all_wordpack(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM wordpack"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'name': row['name'],
                'description': row['description'],
                'price': row['price'],
                'status': row['status'],
                'created_at': row['created_at'],
                'last_update': row['last_update']
            })
        cursor.close()
        return result

    def get_wordpack_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM wordpack WHERE id = {}".format((id))
        cursor.execute(sql, id)
        result = cursor.fetchone()
        cursor.close()
        return result

    def search_wordpack(self, keyword):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM wordpack WHERE name='%"+str(keyword)+"%'"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'name': row['name'],
                'description': row['description'],
                'price': row['price'],
                'status': row['status'],
                'created_at': row['created_at'],
                'last_update': row['last_update']
            })
        cursor.close()
        return result

    ### WORDPAIR ###
    def create_wordpair(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO wordpair VALUES(default, %s, %s, %s, 'ACTIVE')"
        cursor.execute(sql, (data['id_word_pack'], data['word_1'], , data['word_2']))
        cursor.close()
        self.connection.commit()

    def update_wordpair(self, data):
        cursor = self.connection.cursor(dictionary=True)
        first = 1
        sql = "UPDATE wordpair SET "
        if('word_1' in data):
            if(not first):
                sql += ","
            else:
                first = 0
            sql += "word_1 = " + str(data['word_1'])
        if('word_2' in data):
            if(not first):
                sql += ","
            else:
                first = 0
            sql += "word_2 = " + str(data['word_2'])
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

    def delete_wordpair(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "DELETE FROM wordpair WHERE id = {}".format((data['id']))
        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def get_all_wordpair(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM wordpair"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_word_pack': row['id_word_pack'],
                'word_1': row['word_1'],
                'word_2': row['word_2'],
                'status': row['status'],
                'created_at': row['created_at'],
                'last_update': row['last_update']
            })
        cursor.close()
        return result
        
    def get_wordpair_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM wordpair WHERE id = {}".format((id))
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_all_wordpair_by_wordpack_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM wordpair WHERE id_word_pack = {}".format((id))
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_word_pack': row['id_word_pack'],
                'word_1': row['word_1'],
                'word_2': row['word_2'],
                'status': row['status'],
                'created_at': row['created_at'],
                'last_update': row['last_update']
            })
        cursor.close()
        return result

    def get_wordpair_by_wordpack_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        result = {}
        sql = "SELECT * FROM wordpair WHERE id_word_pack = {}".format((id))
        cursor.execute(sql)
        i = random.randrange(0, cursor.rowcount, 1)
        for row in cursor.fetchall():
            if (i == 0):    
                result = {
                    'id': row['id'],
                    'id_word_pack': row['id_word_pack'],
                    'word_1': row['word_1'],
                    'word_2': row['word_2'],
                    'status': row['status'],
                    'created_at': row['created_at'],
                    'last_update': row['last_update']
                }
                break
            i-=1
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
