from nameko.extensions import DependencyProvider

import pymysqlpool
import pymysql

# ========================================================================================
# ----------------------------------- Database Wrapper -----------------------------------
# ========================================================================================

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Constructor")
        self.connection = connection
    
    def get_all_transaction(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM transaction"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_user': row['id_user'],
                'id_word_pack': row['id_word_pack'],
                'type': row['type'],
                'amount': row['amount'],
                'code': row['code'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result
    
    def get_transaction_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM transaction WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result


    def create_transaction(self, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO transaction VALUES(default, %s, %s, %s, %s, %s, default, %s, %s)"
        cursor.execute( sql, 
                        (
                            data['id_user'], 
                            data['id_word_pack'],
                            data['type'],
                            data['amount'],
                            data['code'],
                            data['created_at'],
                            data['updated_at'],
                        )
                    )
        self.connection.commit()

    def update_transaction(self, data):
        pertama=1
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE transaction SET "

        if(data['id_user'] != ""):
            if(not pertama):
                sql += ","
            else:
                pertama = 0
                sql += "id_user = " + "'" + data['id_user'] + "'"
        
        if(data['id_word_pack'] != ""):
            if(not pertama):
                sql += ","
            else:
                pertama = 0
                sql += "id_word_pack = " + "'" + data['id_word_pack'] + "'"

        if(data['amount'] != ""):
            if(not pertama):
                sql += ","
            else:
                pertama = 0
                sql += "amount = " + str(data['amount'])

        if(data['code'] != ""):
            if(not pertama):
                sql += ","
            else:
                pertama = 0
                sql += "code = " + "'" + data['code'] + "'"

        if(data['status'] != ""):
            if(not pertama):
                sql += ","
                sql += "status = " + str(data['status'])
            else:
                pertama = 0
                sql += "status = " + str(data['status'])

        if(data['updated_at'] != ""):
            if(not pertama):
                sql += ","
                sql += "updated_at = " + "'" + data['updated_at'] + "'"
            else:
                pertama = 0
                sql += "updated_at = " + "'" + data['updated_at'] + "'"
                


        sql += " WHERE id = " + str(data['id'])


        cursor.execute(sql)
        cursor.close()
        self.connection.commit()             

    def close_connection(self):
        self.connection.close()
        

# ========================================================================================
# --------------------------------- Dependency Provider ----------------------------------
# ========================================================================================

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        print("DB Dependency Constructor")
        config={'host':'127.0.0.1', 'user':'root', 'password':'', 'database':'soa', 'autocommit':True}
        self.connection_pool = pymysqlpool.ConnectionPool(size=5, name='DB Pool', **config)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def __del__(self):
        print("DB Dependency Destructor")
    
    



