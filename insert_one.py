import sqlite3

db_name = 'test0.db'

try:
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    print(f'Successfully connected to {db_name}')

    q = '''INSERT INTO customers (id, name, email)
            VALUES
            (2, 'Noami','naomimberetta@gmail.com');
        '''

    cursor.execute(q)
    connection.commit()
    print("Record inserted successfully into customers table ", cursor.rowcount)

    cursor.close()

except sqlite3.Error as error:
    print(f'Error while trying to connect to {db_name}. Error: {error}')

finally:
    if connection:
        connection.close()
        print(f'Connection to {db_name} is now closed.')