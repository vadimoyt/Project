import psycopg2
from db_connection import DB_CONNECTION

class Database:


    def __init__(self, host, dbname, user, password, port=5432):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.connection = None

    def db_connection(self):
        self.connection = psycopg2.connect(
            host= self.host,
            port= self.port,
            dbname= self.dbname,
            user= self.user,
            password= self.password
        )
        self.connection.autocommit = True
        return self.connection

    def get_connection(self):
        if self.connection and not self.connection.closed:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute('select 1')
            except psycopg2.OperationalError:
                return self.db_connection()

            return self.connection
        else:
            return self.db_connection()

    def get_cursor(self):
        return self.get_connection().cursor()

    def close_connection(self):
        if self.connection:
            self.connection.close()

db = Database(**DB_CONNECTION)
db.close_connection()


