import sqlite3
from random import randint
from datetime import datetime, timedelta
import names


POSITIONS = [
    "CEO",
    "CTO",
    "Jedi",
    "Padavan",
    "The Grand Master",
    "Mario boy",
    "PM",
    "TL"
]


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)


def create_table(conn):
    with open('sqlite.db', 'w') as db:
        db.write('')
    try:
        create_table_query = "CREATE TABLE employees (\
        'id' INTEGER PRIMARY KEY,\
        'Name' varchar (50),\
        'Position' varchar (50),\
        'HireDate' date,\
        'Salaray' integer (10)\
        )"
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
    except Exception as e:
        print(e)
        if isinstance(e, sqlite3.OperationalError):
            pass
        else:
            conn.close()


def get_random_date():
    days_ago = randint(1, 8943)
    date = datetime.today() - timedelta(days=days_ago)
    return date.strftime("%m/%d/%Y")


def get_random_position():
    return POSITIONS[randint(0, len(POSITIONS) - 1)]


def get_random_salary():
    return randint(0, 999999)


def fill_the_table(conn, _range=50000):
    for i in range(_range):
        try:
            name = names.get_full_name()
            date = get_random_date()
            pos = get_random_position()
            salary = get_random_salary()
            insert_query = "INSERT INTO employees (\
            'Name','Position', 'HireDate','Salaray')\
            VALUES (?,?,?,?);"
            data_tuple = (name, pos, date, salary)
            cursor = conn.cursor()
            cursor.execute(insert_query, data_tuple)
            conn.commit()
        except Exception as e:
            conn.close()
            print(e)
            break


def main():
    connection = create_connection("sqlite.db")
    if connection:
        create_table(connection)
        fill_the_table(connection)
    else:
        pass


if __name__ == "__main__":
    main()
