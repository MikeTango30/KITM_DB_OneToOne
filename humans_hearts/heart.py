import sqlite3


class heart:

    def __init__(self, heart_id, volume, blood_pump_rate, creation_date, defect):
        self.__heart_id = heart_id
        self.__volume = volume
        self.__blood_pump_rate = blood_pump_rate
        self.__creation_date = creation_date
        self.__defect = defect
        self.__db_name = "humanHearts.db"

    # getters & setters
    def get_id(self):
        return self.__heart_id

    def set_id(self, value):
        self.__heart_id = value

    def get_volume(self):
        return self.__volume

    def set_volume(self, value):
        self.__volume = value

    def get_blood_pump_rate(self):
        return self.__blood_pump_rate

    def set_blood_pump_rate(self, value):
        self.__blood_pump_rate = value

    def get_creation_date(self):
        return self.__creation_date

    def set_creation_date(self, value):
        self.__creation_date = value

    def get_defect(self):
        return self.__defect

    def set_defect(self, value):
        self.__defect = value

    def set_db_name(self, value):
        self.__db_name = value

    # crud
    def execute_query(self, query, params, select=None):
        try:
            connection = sqlite3.connect(self.__db_name)
            cursor = connection.cursor()

            if select is not None:
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

    def create_heart(self, human_id):
        query = "INSERT INTO hearts VALUES(?, ?, ?, ?, ?, ?)"
        params = (None, human_id, self.__volume, self.__blood_pump_rate, self.__creation_date, self.__defect)
        self.execute_query(query, params)

    def get_record_id(self, human_id):
        query = "SELECT heart_id FROM hearts WHERE human_id = (?)"
        params = (human_id, )
        return self.execute_query(query, params, True)

    def update_record_(self, field, value):
        query = "UPDATE hearts SET " + field + " = (?) WHERE heart_id = (?)"
        params = (value, self.__heart_id)
        self.execute_query(query, params)

    # TODO delete