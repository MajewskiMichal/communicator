import argparse

from libs.db import connect_to_db, close_connection
from libs.user import User


def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", action="store", dest="username",
                        help="User login")
    parser.add_argument("-p", "--password", action="store", dest="password",
                        help="User password")
    parser.add_argument("-n", "--new-password", action="store", dest="new_password",
                        help="New user password")
    parser.add_argument("-l", "--list", action="store_true", dest="list", default=False,
                        help="Get users list")
    parser.add_argument("-d", "--delete", action="store", dest="delete",
                        help="Delete user")
    parser.add_argument("-e", "--edit", action="store", dest="edit",
                        help="Edit user")
    options = parser.parse_args()
    return options


def manage_users():
    options = set_options()
    # kodzik tutaj

    cnx, cursor = connect_to_db()

    # u = User()
    # u.username = 'janusz'
    # u.email = 'janusz@gmail.com'
    # u.set_password('passat_b5', '1999')
    # u.save_to_db(cursor)

    u = User.load_user_by_id(cursor, 1)
    print(u.id)
    print(u.email)
    print(u.username)

    close_connection(cnx, cursor)


if __name__ == "__main__":
    manage_users()