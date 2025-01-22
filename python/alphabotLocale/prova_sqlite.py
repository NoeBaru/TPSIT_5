import sqlite3

# connessione al database
conn = sqlite3.connect('mioDatabase.db')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE sedeA (
                comandi VARCHAR(1) NOT NULL UNIQUE,
                str_mov TEXT NOT NULL,
                PRIMARY KEY (comandi),
            );
            ''')
conn.commit()
variabile_in_stampa = cur.fetchall()
# conn.close()