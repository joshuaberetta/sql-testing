import sqlite3

db_name = 'test1.db'

try:
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    print(f'Successfully connected to {db_name}')

    q = '''CREATE TABLE contacts (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE);
        '''

    cursor.execute(q)
    connection.commit()
    print('Table successfully created')

    cursor.close()

except sqlite3.Error as error:
    print(f'Error while trying to connect to {db_name}. Error: {error}')

finally:
    if connection:
        connection.close()
        print(f'Connection to {db_name} is now closed.')