import sqlite3
import pprint
from Humans_Hearts.heart import heart
from Humans_Hearts.human import human


# One to One rel
# Human: human_id, first_name, last_name, birth_date
# Heart: heart_id, creation_date, volume, defect, blood_pump_rate

humans = 'humans'
hearts = 'hearts'
# queries for creating tables
create_table_humans = """CREATE TABLE IF NOT EXISTS humans (
                                                        human_id integer PRIMARY KEY,
                                                        heart_id integer UNIQUE,
                                                        first_name text NOT NULL,
                                                        last_name text NOT NULL,
                                                        birth_date date NOT NULL,
                                                        FOREIGN KEY (heart_id) REFERENCES hearts(heart_id)
                                                        ON UPDATE CASCADE
                                                        )"""

create_table_hearts = """CREATE TABLE IF NOT EXISTS hearts (
                                                        heart_id integer PRIMARY KEY,
                                                        human_id integer UNIQUE,
                                                        volume number NOT NULL,
                                                        blood_pump_rate number NOT NULL,
                                                        creation_date date NOT NULL,
                                                        defect text NOT NULL DEFAULT 'none',
                                                        FOREIGN KEY (human_id) REFERENCES humans(human_id)
                                                        ON UPDATE CASCADE
                                                        )"""

db_name = "humanHearts.db"


# db conn
def open_connection():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    return connection, cursor


def close_connection(connection, cursor):
    cursor.close()
    connection.close()


def create_table(create_table_query):
    try:
        connection, cursor = open_connection()
        cursor.execute(create_table_query)
        connection.commit()
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        # noinspection PyUnboundLocalVariable
        close_connection(connection, cursor)


# crud
# -------
# helpers
def get_fields(entity):
    field_values = [attr + ' = (?)' for attr, value in entity.__dict__.items()]

    return field_values


def execute_query(sql_query, query_parameters=None, select=None):
    try:
        connection, cursor = open_connection()

        if select is None:
            cursor.execute(sql_query, query_parameters)
            connection.commit()
        if select:
            rows = [row for row in cursor.execute(sql_query)]
            return rows
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        # noinspection PyUnboundLocalVariable
        close_connection(connection, cursor)


def gather_parameters(entity):
    parameters = [value for attr, value in entity.__dict__.items()]

    return parameters


create_table(create_table_humans)
create_table(create_table_hearts)















