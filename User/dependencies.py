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
        sql = "INSERT INTO users VALUES(default, %s, %s, %s, %s, %s,'CREATED', %s, %s)"
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
                        )
                    )
        self.connection.commit()

    def update_user(self, id, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE users SET email = %s, password = %s, name = %s, gender = %s, dob = %s, status = %s, created_at = %s, updated_at = %s WHERE id = %s"
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
                            id
                        )
                    )
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

    def update_user_wordpack(self, id, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE user_word_packs SET id_user = %s, id_word_pack = %s, created_at = %s, updated_at = %s WHERE id = %s"
        cursor.execute( sql, 
                        (
                            data['id_user'], 
                            data['id_word_pack'], 
                            data['created_at'],
                            data['updated_at'],
                            id
                        )
                    )
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