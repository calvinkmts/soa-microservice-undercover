from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Constructor")
        self.connection = connection

    def create_round(self, id_game, round, word1, word2, num_mr_white, num_civilian, num_undercover):
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO game_round VALUES(default, %s, %s, %s, %s, %s, %s, %s, 1)"
        cursor.execute( sql, (id_game, round, word1, word2, num_mr_white, num_civilian, num_undercover))
        self.connection.commit()

    def update_round(self, id, round, num_mr_white, num_civilian, num_undercover):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE game_round SET round = %s, num_mr_white = %s, num_civilian =%s, num_undercover = %s  WHERE id = %s"
        cursor.execute( sql, (round, num_mr_white, num_civilian, num_undercover, id))
        cursor.close()
        self.connection.commit()

    def delete_round(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE game_round SET status = 0 WHERE id = {}".format(id)
        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def get_all_round(self):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM game_round"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_round_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM game_round where id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_word1(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT word1 FROM game_round WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_word2(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT word2 FROM game_round WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def close_connection(self):
        self.connection.close()

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        print("DB Dependency Constructor")
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="DB_POOL",
                pool_size=10,
                pool_reset_session=True,
                host='localhost',
                database='soa_ceria',
                user='root',
                password=''
            )
            print ("Success Connecting to MySQL")
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())

    def __del__(self):
        print("DB Dependency Destructor")