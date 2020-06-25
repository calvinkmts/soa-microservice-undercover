from nameko.extensions import DependencyProvider
from datetime import datetime
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
                'typee': row['type'],
                'amount': row['amount'],
                'code': row['code'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        print(result[0]['created_at'])
        return result
    
    def get_transaction_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM transaction WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result


    # def create_transaction(self,data):
    #     cursor = self.connection.cursor(pymysql.cursors.DictCursor)
    #     sql = "INSERT INTO transaction VALUES(default, %s, %s, %s, %s, %s,%s, %s)"
    #     cursor.execute( sql, 
    #                     (
    #                         data['id_user'], 
    #                         data['id_word_pack'],
    #                         data['type'],
    #                         data['amount'],
    #                         data['code'],
    #                         data['created_at'],
    #                         data['updated_at'],
    #                     )
    #                 )
    #     print(sql)
    #     self.connection.commit()

    def create_transaction(self,data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO `transaction` (`id`"
        sql2 = "VALUES(default"
        if('id_user' in data):
            sql += "," + "`id_user`"
            sql2 += "," + str(data['id_user'])
        if('id_word_pack' in data):
            sql += "," + "`id_word_pack`"
            sql2 += "," + str(data['id_word_pack'])
        if('amount' in data):
            sql += "," + "`amount`"
            sql2 += "," + str(data['amount'])

        sql += ",`created_at`)"
        sql2 += ",CURRENT_TIMESTAMP)"
        abc = sql+sql2
        cursor.execute(abc)
        print(abc)
        self.connection.commit()           

    def update_transaction(self, data):
        pertama=1
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE transaction SET "

        if('id_user' in data):
            if(not pertama):
                sql += ","
            else:
                pertama = 0
                sql += "id_user = " + "'" + str(data['id_user']) + "'"
        
        if('id_word_pack' in data):
            if(not pertama):
                sql += ","
                sql += "id_word_pack = " + "'" + str(data['id_word_pack']) + "'"
            else:
                pertama = 0
                sql += "id_word_pack = " + "'" + str(data['id_word_pack']) + "'"

        if('amount' in data):
            if(not pertama):
                sql += ","
                sql += "amount = " + "'" + str(data['amount']) + "'"
            else:
                pertama = 0
                sql += "amount = " + "'" + str(data['amount']) + "'"
        
        if('created_at' in data):
            if(not pertama):
                sql += ","
                sql += "created_at = " + "'" + str(data['created_at']) + "'"
            else:
                pertama = 0
                sql += "created_at = " + "'" + str(data['created_at']) + "'"
     
        sql += " WHERE id = " + str(data['id'])

        print(sql)
        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def delete_transaction(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE FROM transaction WHERE id = {}".format(id)
        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

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
        if('redeemed_by' in data):
            if(not pertama):
                sql += ","
            else:
                pertama = 0
                sql += "redeemed_by = " + str(data['redeemed_by'])
        if('code' in data):
            if(not pertama):
                sql += ","
                sql += "code = " + "'" + data['code'] + "'"
            else:
                pertama = 0
                sql += "code = " + "'" + data['code'] + "'"
        if('amount' in data):
            if(not pertama):
                sql += ","
                sql += "amount = " + str(data['amount'])
            else:
                pertama = 0
                sql += "amount = " + str(data['amount'])
        if('status' in data):
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

    def delete_voucher(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE FROM voucher WHERE id = {}".format(id)
        cursor.execute(sql)
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
        self.connection_pool = pymysqlpool.ConnectionPool(size=10, name='DB Pool', **config)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def __del__(self):
        print("DB Dependency Destructor")
    
    



