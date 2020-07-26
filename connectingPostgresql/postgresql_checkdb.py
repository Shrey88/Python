import postgresql_connection

conn = postgresql_connection.get_connection()

conn_cur = conn.cursor()

""" ===================================================================
    how to get the datetime in the timezone format
======================================================================= """
# conn_cur.execute("SELECT * FROM history")
# records = conn_cur.fetchall()
#
# for record in records:
#     print("{} \t {} \t {}".format(record[0], record[0].astimezone(), type(record[0])))
