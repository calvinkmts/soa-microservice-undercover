from nameko.extensions import DependencyProvider

import pymysqlpool
import pymysql

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Constructor")
        self.connection = connection
    
    def create_user(self, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO users VALUES(default, %s, %s, %s, %s, %s,'CREATED', %s, %s, %s)"
        cursor.execute( sql, 
                        (
                            data['email'], 
                            data['password'], 
                            data['name'],
                            data['gender'],
                            data['dob'],
                            data['status'],
                            data['created_at'],
                            data['updated_at'],
                            data['balance']
                        )
                    )
        self.connection.commit()

    def update_user(self, data):
        tanda=1
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE users SET "
        if('email' in data):
            if(not tanda):
                sql+= ","
            else:
                tanda=0
                sql+= "email = " + str(data['email'])
        if('password' in data):
            if(not tanda):
                sql+= ","
                sql+= "password = " + str(data['password'])
            else:
                tanda=0
                sql+= "password = " + str(data['password'])
        if('name' in data):
            if(not tanda):
                sql+= ","
                sql+= "name = " + str(data['name'])
            else:
                tanda=0
                sql+= "name = " + str(data['name'])
        if('gender' in data):
            if(not tanda):
                sql+= ","
                sql+= "gender = " + str(data['gender'])
            else:
                tanda=0
                sql+= "gender = " + str(data['gender'])
        if('dob' in data):
            if(not tanda):
                sql+= ","
                sql+= "dob = " + str(data['dob'])
            else:
                tanda=0
                sql+= "dob = " + str(data['dob'])
        if('status' in data):
            if(not tanda):
                sql+= ","
                sql+= "status = " + str(data['status'])
            else:
                tanda=0
                sql+= "status = " + str(data['status'])
        if('created_at' in data):
            if(not tanda):
                sql+= ","
                sql+= "created_at = " + str(data['created_at'])
            else:
                tanda=0
                sql+= "created_at = " + str(data['created_at'])
        if('updated_at' in data):
            if(not tanda):
                sql+= ","
                sql+= "updated_at = " + str(data['updated_at'])
            else:
                tanda=0
                sql+= "updated_at = " + str(data['updated_at'])
        if('balance' in data):
            if(not tanda):
                sql+= ","
                sql+= "balance = " + str(data['balance'])
            else:
                tanda=0
                sql+= "balance = " + str(data['balance'])
        
        sql+= " WHERE id = " + str(data['id'])
        cursor.execute(sql)
        self.connection.commit()

    def get_all_user(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'email': row['email'],
                'password': row['password'],
                'name': row['name'],
                'gender': row['gender'],
                'dob': row['dob'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result
    
    def get_user_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM users WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def set_user_active(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE users SET status = 'ACTIVE' WHERE id = %s"
        cursor.execute(sql, (id))
        cursor.close()
        self.connection.commit()

    def create_user_wordpack(self, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO user_word_packs VALUES(default, %s, %s, %s, %s)"
        cursor.execute( sql, 
                        (
                            data['id_user'], 
                            data['id_word_pack'], 
                            data['created_at'],
                            data['updated_at'],
                        )
                    )
        self.connection.commit()

    def update_user_wordpack(self, data):
        tanda=1
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE user_word_packs SET "
        if('id_user' in data):
            if(not tanda):
                sql+= ","
            else:
                tanda=0
                sql+= "id_user = " + str(data['id_user'])
        if('id_word_pack' in data):
            if(not tanda):
                sql+= ","
                sql+= "id_word_pack = " + str(data['id_word_pack'])
            else:
                tanda=0
                sql+= "id_word_pack = " + str(data['id_word_pack'])
        if('created_at' in data):
            if(not tanda):
                sql+= ","
                sql+= "created_at = " + str(data['created_at'])
            else:
                tanda=0
                sql+= "created_at = " + str(data['created_at'])
        if('updated_at' in data):
            if(not tanda):
                sql+= ","
                sql+= "updated_at = " + str(data['updated_at'])
            else:
                tanda=0
                sql+= "updated_at = " + str(data['updated_at'])
        sql+= " WHERE id = " + str(data['id'])
        cursor.execute(sql)
        self.connection.commit()

    def get_all_user_wordpack(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM user_word_packs"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_user': row['id_user'],
                'id_word_pack': row['id_word_pack'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result
    
    def get_user_wordpack_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM user_word_packs WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def get_all_user_wordpack_by_user_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM user_word_packs WHERE id_user = {}".format(id)
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_user': row['id_user'],
                'id_word_pack': row['id_word_pack'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result


    def close_connection(self):
        self.connection.close()

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        print("DB Dependency Constructor")
        config={'host':'127.0.0.1', 'user':'root', 'password':'', 'database':'proyeksoa', 'autocommit':True}
        self.connection_pool = pymysqlpool.ConnectionPool(size=5, name='DB Pool', **config)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def __del__(self):
        print("DB Dependency Destructor")