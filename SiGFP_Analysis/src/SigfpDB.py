import pyodbc
from configparser import ConfigParser
from pyodbc import Connection, Cursor
from fileParsing import FileParsing


class SigfpDB(object):

    def __init__(self):
        self._parser = None
        self._conn = None
        self._cursor = None

    def _db_connect(self):
        try:
            kwargs = FileParsing.parse_file(filename='..\\_connection\\sqlserver_connection.ini',
                                            section='SQL_SERVER_CONNECTION', outputformat='Dict')

            if kwargs.__len__() > 0:
                print("Connecting to database......")
                self._conn = pyodbc.connect(**kwargs)

            return self._conn
        except(Exception, pyodbc.DatabaseError) as error:
            print(error)

    def _close_connection(self, cursor):
        self._cursor = cursor
        try:
            if self._cursor is not None:
                self._cursor.close()
                print("Cursor is closed........")

            if self._conn is not None:
                self._conn.close()
                print("Database connection is closed.......")

        except(Exception, pyodbc.DatabaseError) as error:
            print(error)

    def get_conn(self):
        return self._db_connect()

    def close_conn(self, cursor):
        self._close_connection(cursor)
