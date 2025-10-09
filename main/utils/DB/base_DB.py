import mysql.connector
from main.utils.log.logger import Logger

class BaseDB:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def create_connection(self):
        Logger.log(f'[info] ▶ connect to {self.database} database')
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

    def close_connection(self):
        Logger.log('[info] ▶ close connection to database')
        self.connection.close()

    def sql_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            response = cursor.fetchall()
            self.connection.commit()
            return response
        except mysql.connector.Error as err:
            Logger.log(f'[erro]   {err}')

    def sql_select(self, tableName, target='*', conditions=''):
        Logger.log(f'[info] ▶ select "{target}" from "{tableName}" table:')
        query = f'SELECT {target} FROM {tableName} {conditions};'
        response = self.sql_query(query)
        if len(response) == 1:
            if len(response[0]) == 1:
                Logger.log(f'[info]   result is: "{response[0][0]}"')
            else:
                Logger.log(f'[info]   result is: "{response[0]}"')
        else:
            Logger.log(f'[info]   result is: "{response}"')
        
        return response
    
    def sql_insert(self, tableName, target='', values=''):
        Logger.log(f'[info] ▶ insert into "{tableName}" table values {values}')
        query = f"INSERT INTO {tableName} ({target}) VALUES ({values});"
        self.sql_query(query)