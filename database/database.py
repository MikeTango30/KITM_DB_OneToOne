import sqlite3
from humans_hearts.heart import heart
from humans_hearts.human import human

# repo
human1 = human(None, 'Peter', 'Nohart', '1972-12-24')
heart1 = heart(None, 3.7, 70, 'NA', '2015-12-08')
human2 = human(None, 'Norton', 'Fewhart', '1986-11-24')
heart2 = heart(None, 4.6, 60, 'NA', '2016-12-09')
human3 = human(None, 'Gabriel', 'Lesshart', '1974-10-24')
heart3 = heart(None, 2.6, 65, 'NA', '2017-12-12')
human4 = human(None, 'Mustafa', 'Cloghart', '1992-08-24')
heart4 = heart(None, 3.5, 75, 'NA', '2018-12-01')
human5 = human(None, 'Igor', 'Nopumpinhart', '1993-02-24')
heart5 = heart(None, 4.7, 74, 'NA', '2019-11-18')
human6 = human(None, 'Jermaine', 'Slightearinhart', '2000-02-24')
heart6 = heart(None, 6.6, 69, 'NA', '2018-10-16')
human7 = human(None, 'Alius', 'Oldhart', '1988-01-24')
heart7 = heart(None, 2.9, 81, 'NA', '2016-09-12')
human8 = human(None, 'Toby', 'Freshart', '1945-05-24')
heart8 = heart(None, 4.7, 66, 'NA', '2015-06-13')
human9 = human(None, 'Hannibal', 'Noblehart', '1999-04-24')
heart9 = heart(None, 4.3, 72, 'NA', '2014-01-02')
human10 = human(None, 'Thor', 'Cancerhart', '2010-06-24')
heart10 = heart(None, 5.5, 80, 'NA', '2017-06-22')

humans = [human1, human2, human3, human4, human5, human6, human7, human8, human9, human10]
hearts = [heart1, heart2, heart3, heart4, heart5, heart6, heart7, heart8, heart9, heart10]


db_name = "humanHearts.db"
# queries for creating tables
create_table_humans = """CREATE TABLE IF NOT EXISTS humans (
                                                        human_id integer PRIMARY KEY,
                                                        heart_id integer,
                                                        first_name text NOT NULL,
                                                        last_name text NOT NULL,
                                                        birth_date date NOT NULL,
                                                        FOREIGN KEY (heart_id) REFERENCES hearts(heart_id)
                                                        ON UPDATE CASCADE
                                                        )"""

create_table_hearts = """CREATE TABLE IF NOT EXISTS hearts (
                                                        heart_id integer PRIMARY KEY,
                                                        human_id integer,
                                                        volume number NOT NULL,
                                                        blood_pump_rate number NOT NULL,
                                                        creation_date date NOT NULL,
                                                        defect text NOT NULL DEFAULT 'none',
                                                        FOREIGN KEY (human_id) REFERENCES humans(human_id)
                                                        ON UPDATE CASCADE
                                                        )"""


def create_table(create_table_query):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        # noinspection PyUnboundLocalVariable
        cursor.close()
        connection.close()


def execute_select_query(query):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        rows = cursor.execute(query).fetchall()
        return rows
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        # noinspection PyUnboundLocalVariable
        cursor.close()
        connection.close()

create_table(create_table_humans)
create_table(create_table_hearts)


def create_human_heart(human, heart):
    heart_id = 'heart_id'
    human.create_human()
    human.set_id(human.get_record_id())
    heart.create_heart(human.get_id())
    heart.set_id(heart.get_record_id(human.get_id()))
    human.update_record_(heart_id, heart.get_id())


# create_human_heart(human1, heart1)
# create_human_heart(human2, heart2)
# create_human_heart(human3, heart3)
# create_human_heart(human4, heart4)
# create_human_heart(human5, heart5)
# create_human_heart(human6, heart6)
# create_human_heart(human7, heart7)
# create_human_heart(human8, heart8)
# create_human_heart(human9, heart9)
# create_human_heart(human10, heart10)

print(execute_select_query("SELECT * FROM humans, hearts"))














