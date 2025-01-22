import sqlite3

DB_NAME = 'account.db'

def createDatabase():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS account (
            utente VARCHAR(30) NOT NULL PRIMARY KEY,
            password VARCHAR(20) NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    createDatabase()
