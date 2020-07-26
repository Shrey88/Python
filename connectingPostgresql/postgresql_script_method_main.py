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

    email_id = "f_beardon@gmail.com"
    country = input("Enter the country name: ")

    update_query = """UPDATE person SET email='{}' 
    WHERE country_of_birth='{}'""".format(email_id, country)

    """
        there is nothing like executescript method in postgresql
    """
    conn_cursor.execute(update_query)

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
