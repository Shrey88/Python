import postgresql_connection

if __name__ == "__main__":
    """ get the database connection object"""
    conn = postgresql_connection.get_connection()

    print(type(conn))
    """
        Creating a cursor

        this cursor allows us to read/modify our database. 
    """
    conn_cursor = conn.cursor()
    print(type(conn_cursor))

    """
        Parameterized Query : 1
        update query with the hardcoded values
    """
    # update_query = """UPDATE person SET email='fernandab@gmail.comoros'
    #                 WHERE person_uid='ecafaccd-0937-433a-a76b-76a41c24ad7c'"""

    # conn_cursor.execute(update_query)

    """
        Parameterized Query : 2
        update query using variable
    """
    email_id = "f_beardon_1@gmail.co.or"
    country = "OakWood"
    # update_query = """UPDATE person SET email='{}', country_of_birth='{}'
    # WHERE person_uid='ecafaccd-0937-433a-a76b-76a41c24ad7c'""".format(email_id, country)

    # conn_cursor.execute(update_query)

    """
        Parameterized Query : 3
        update query using variable, but the variables will be passed to execute method as tuple 
    """
    # update_query = """UPDATE person SET email= %s, country_of_birth= %s
    #  WHERE person_uid='ecafaccd-0937-433a-a76b-76a41c24ad7c'"""
    #
    # conn_cursor.execute(update_query, (email_id, country))

    """
        Parameterized Query : 4
        update query using variable, but the variables will be passed to execute method as tuple
        so when you are passing the single value to be updated in tuple, you need to add comma after that argument
    """
    bod = input("Enter date of birth in yyyy-mm-dd format: ")

    update_query = """UPDATE person SET date_of_birth=Date %s
         WHERE person_uid='ecafaccd-0937-433a-a76b-76a41c24ad7c'"""

    conn_cursor.execute(update_query, (bod, ))

    conn_cursor.connection.commit()

    """
        Executing the query        
        it will just execute the query
    """
    select_query = "SELECT * FROM person;"

    conn_cursor.execute(select_query)

    """ Fetching the records"""
    records = conn_cursor.fetchall()

    """ Printing the records"""
    for record in records:
        print(record)

    postgresql_connection.close_connection(conn_cursor, conn)
