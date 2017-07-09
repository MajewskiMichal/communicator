class User:
    def __init__(self):
        self.__id = -1
        self.email = ""
        self.username = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password, salt):
        self.__hashed_password = password + salt

    def save_to_db(self, cursor):
        if self.__id == -1:
            sql = 'INSERT INTO User(email, username, hashed_password) VALUES (%s, %s, %s);'
            params = (self.email, self.username, self.__hashed_password)
            cursor.execute(sql, params)
            self.__id = cursor.lastrowid
            return True
        return False

    @staticmethod
    def load_user_by_id(cursor, id):
        sql = 'SELECT * FROM User WHERE id=%s;'
        params = (id,)
        cursor.execute(sql, params)
        data = cursor.fetchone()

        if data is not None:
            u = User()
            u.__id = data[0]
            u.email = data[1]
            u.username = data[2]
            u.__hashed_password = data[3]
            return u
        return None

    @staticmethod
    def load_all_users(cursor):
        sql = 'SELECT * FROM User;'
        cursor.execute(sql)
        data = cursor.fetchall()

        users = list()
        for user in data:
            u = User()
            u.__id = user[0]
            u.email = user[1]
            u.username = user[2]
            u.__hashed_password = user[3]
            users.append(u)
        return users