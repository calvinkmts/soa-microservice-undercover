from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Constructor")
        self.connection = connection

    ## UTILITY ##

    def check_win(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM round_detail "
        sql += " JOIN game_round ON round_detail.id_round = game_round.id "
        sql += " WHERE game_round.word_1 = %s AND game_round.id = %s"
        cursor.execute(sql, (data['word1'], data['id']))
        result = cursor.fetchone()
        cursor.close()
        return result

    def mrwhite_guess(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM turn_detail "
        sql += " JOIN round_detail ON turn_detail.id_round_detail = round_detail.id "
        sql += " JOIN game_round ON round_detail.id_round = game_round.id "
        sql += " WHERE game_round.id = %s AND word1 = %s"
        cursor.execute(sql, (data['id'], data['word1']))
        result = cursor.fetchone()
        cursor.close()
        return result

    ## GAME ROUND ##

    def create_round(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO game_round VALUES(default, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute( sql, (data['id_game'], data['round'], data['word1'], data['word2'], data['num_mr_white'], data['num_civilian'], data['num_undercover']))
        self.connection.commit()

    def update_round(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE game_round SET round = %s, word1 = %s, word2 = %s, num_mr_white = %s, num_civilian =%s, num_undercover = %s WHERE id = %s"
        cursor.execute( sql, (data['round'], data['word1'], data['word2'], data['num_mr_white'], data['num_civilian'], data['num_undercover'], data['id']))
        cursor.close()
        self.connection.commit()

    def delete_round(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "DELETE FROM game_round WHERE id = {}".format(id)
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

    ## ROUND DETAIL ##

    def create_round_detail(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO round_detail VALUES(default, %s, %s, %s, ALIVE)"
        cursor.execute( sql, (data['id_round'], data['id_user'], data['id_role']))
        self.connection.commit()

    def update_round_detail(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE round_detail SET condition = %s WHERE id = %s AND id_user = %s"
        cursor.execute( sql, (data['condition'], data['id'], data['id_user']))
        cursor.close()
        self.connection.commit()

    def delete_round_detail(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "DELETE FROM round_detail WHERE id = {}".format(id)
        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def get_all_round_detail(self):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM round_detail"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_round_detail_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM round_detail WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_round_detail_by_round_id(self, id_round):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM round_detail WHERE id_round = {}".format(id_round)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_all_alive_player(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM round_detail WHERE condition = 'ALIVE' AND id_round = {}".format(data['id_round'])
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    ## TURN DETAIL ##

    def create_turn_detail(self, data):
        if('user_word' not in data):
            data['user_word'] = None
        if('user_desc' not in data):
            data['user_desc'] = None
        if('user_vote' not in data):
            data['user_vote'] = None
        if('status' not in data):
            data['status'] = None
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO turn_detail VALUES(default, %s, %s, %s, %s, None, %s)"
        cursor.execute( sql, (data['id_round_detail'], data['turn'], data['user_word'], data['user_desc'], data['status']))
        self.connection.commit()

    def update_turn_detail(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE turn_detail SET user_word = %s, user_desc = %s, status = %s WHERE id = %s AND id_round_detail = %s"
        cursor.execute( sql, (data['user_word'], data['user_desc'], data['status'], data['id'], data['id_round_detail']))
        cursor.close()
        self.connection.commit()

    def update_turn_detail_user_word(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE turn_detail SET user_desc = %s WHERE id = %s AND id_round_detail = %s"
        cursor.execute( sql, (data['user_desc'], data['id'], data['id_round_detail']))
        cursor.close()
        self.connection.commit()

    def update_turn_detail_user_desc(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE turn_detail SET user_desc = %s WHERE id = %s AND id_round_detail = %s"
        cursor.execute( sql, (data['user_desc'], data['id'], data['id_round_detail']))
        cursor.close()
        self.connection.commit()

    def update_turn_detail_user_vote(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE turn_detail SET user_vote = %s WHERE id = %s AND id_round_detail = %s"
        cursor.execute( sql, (data['user_vote'], data['id'], data['id_round_detail']))
        cursor.close()
        self.connection.commit()    

    def update_turn_detail_status(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE turn_detail SET status = %s WHERE id = %s AND id_round_detail = %s"
        cursor.execute( sql, (data['status'], data['id'], data['id_round_detail']))
        cursor.close()
        self.connection.commit()

    def delete_turn_detail(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "DELETE FROM turn_detail WHERE id = {}".format(id)
        cursor.execute(sql)
        cursor.close()
        self.connection.commit()

    def get_all_turn_detail(self):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM turn_detail"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_turn_detail_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM turn_detail WHERE id = {}".format(id)
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