import psycopg2
# from postgresql_config_manager import get_connection_from_config
import postgresql_config_manager


def get_connection():
    """ Connect to the Postgresql database server """
    conn = None
    try:
        """ Read connection parameters"""
        params = postgresql_config_manager.get_connection_string_from_config()

        """ Connect to the Postgresql server """
        print('Connecting to the Postgresql database....')
        conn = psycopg2.connect(**params)

        """ 
            Create a cursor
            
            this cursor allows us to read/modify our database. 
        """
        # cur = conn.cursor()

        """ Execute a statement """
        # print('Postgresql database version: ')
        # cur.execute("SELECT version();")

        """ display the Postgresql database server version """
        # db_version = cur.fetchone()
        # print(db_version)

        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('Database connection is closed')


def close_connection(cursor, connection):
    try:
        """ close the communication with the Postgresql """
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection is closed')
