import sqlite3


class human:

    def __init__(self, human_id, first_name, last_name, birth_date):
        self.__human_id = human_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__db_name = "humanHearts.db"

    # getters & setters
    def get_id(self):
        return self.__human_id

    def set_id(self, value):
        self.__human_id = value

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, value):
        self.__first_name = value

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, value):
        self.__last_name = value

    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, value):
        self.__birth_date = value

    def set_db_name(self, value):
        self.__db_name = value

    # crud
    def execute_query(self, query, params, select=None):
        try:
            connection = sqlite3.connect(self.__db_name)
            cursor = connection.cursor()

            if select:
                record_id = cursor.execute(query, params).fetchone()[0]
                return record_id

            cursor.execute(query, params)
            connection.commit()
        except sqlite3.DatabaseError as error:
            print(error)
        finally:
            # noinspection PyUnboundLocalVariable
            cursor.close()
            connection.close()

    def create_human(self):
        query = "INSERT INTO humans VALUES(?, ?, ?, ?, ?)"
        params = (None, None, self.__first_name, self.__last_name, self.__birth_date)
        self.execute_query(query, params)

    def get_record_id(self):
        query = "SELECT human_id FROM humans WHERE first_name = (?) AND last_name = (?) AND birth_date = (?)"
        params = (self.__first_name, self.__last_name, self.__birth_date)
        return self.execute_query(query, params, True)

    def update_record_(self, field, value):
        query = "UPDATE humans SET " + field + " = (?) WHERE human_id = (?)"
        params = (value, self.__human_id)
        self.execute_query(query, params)

    # TODO delete
