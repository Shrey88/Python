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
        Executing the query        
        it will just execute the query
    """
    # select_query = "SELECT * FROM person;"
    #
    # conn_cursor.execute(select_query)

    """
        Parameterized Query : 1
        when you want to search for the records matching the condition
        so here the catch is that in tuple you cannot just give the single value, 
        so you need to put comma after the argument
    """
    condition = input("Enter the country name: ")
    select_query = "SELECT * FROM person WHERE country_of_birth=%s;"

    conn_cursor.execute(select_query, (condition, ))

    """ Fetching the records"""
    records = conn_cursor.fetchall()

    """ Printing the records"""
    for record in records:
        print(record)

    postgresql_connection.close_connection(conn_cursor, conn)
