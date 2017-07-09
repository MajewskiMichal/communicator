from mysql.connector import connect


def connect_to_db():  # cnx, cursor
    cnx = connect(
        user='root',
        password='pass',
        database='communicator_db'
    )
    cursor = cnx.cursor()

    return cnx, cursor


def close_connection(cnx, cursor):
    cursor.close()
    cnx.close()
