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
    
    def get_all_voucher(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM voucher"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'redeemed_by': row['redeemed_by'],
                'code': row['code'],
                'amount': row['amount'],
                'status': row['status']
            })
        cursor.close()
        return result
    
    def get_voucher_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM voucher WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def search_voucher(self, code):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM voucher WHERE code = " + "'" + code + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def create_voucher(self, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO voucher VALUES(default, default, %s, %s, default)"
        cursor.execute( sql, 
                        (
                            data['code'], 
                            data['amount']
                        )
                    )
        self.connection.commit()

    def update_voucher(self, data):
        pertama=1
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE voucher SET "
        if(data['redeemed_by'] != ""):
            if(not pertama):
                sql += ","
            else:
                pertama = 0
                sql += "redeemed_by = " + str(data['redeemed_by'])
        if(data['code'] != ""):
            if(not pertama):
                sql += ","
                sql += "code = " + "'" + data['code'] + "'"
            else:
                pertama = 0
                sql += "code = " + "'" + data['code'] + "'"
        if(data['amount'] != ""):
            if(not pertama):
                sql += ","
                sql += "amount = " + str(data['amount'])
            else:
                pertama = 0
                sql += "amount = " + str(data['amount'])
        if(data['status'] != ""):
            if(not pertama):
                sql += ","
                sql += "status = " + str(data['status'])
            else:
                pertama = 0
                sql += "status = " + str(data['status'])

        sql += " WHERE id = " + str(data['id'])


        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def delete_voucher(self, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE FROM voucher WHERE id = %s"
        cursor.execute(sql, 
                        (   
                            data['id']
                        )
                    )
        cursor.close()
        self.connection.commit()

                


    def redeem_voucher(self, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE voucher SET redeemed_by = %s, status = 0 WHERE code = %s AND status = 1"
        cursor.execute(sql, 
                        (   
                            data['redeemed_by'],
                            data['code']
                        )
                    )
        cursor.close()
        self.connection.commit()
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
        config={'host':'127.0.0.1', 'user':'root', 'password':'', 'database':'soa', 'autocommit':True}
        self.connection_pool = pymysqlpool.ConnectionPool(size=5, name='DB Pool', **config)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def __del__(self):
        print("DB Dependency Destructor")
    
    



