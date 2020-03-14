import sqlite3
from uuid import uuid4
from random import randint

db_name = 'test1.db'
details = [
    ['Naomi', 'naomimberetta@gmail.com'],
    ['Peter', 'peter@umoyta.net']
]

def insert_row(connection, cursor, name, email):

    q = '''INSERT INTO contacts (id, name, email)
            VALUES
            (?, ?, ?);
        '''
    
    try:
        cursor.execute(q, (str(uuid4()), name, email))
        connection.commit()
        print("Record inserted successfully into contacts table ", cursor.rowcount)
        # return cursor
    except sqlite3.Error as error:
        raise error

    
try:
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    print(f'Successfully connected to {db_name}')

    for detail in details:
        insert_row(connection, cursor, *detail)

    cursor.close()

except sqlite3.Error as error:
    print(f'Error while trying to connect to {db_name}. Error: {error}')

finally:
    if connection:
        connection.close()
        print(f'Connection to {db_name} is now closed.')