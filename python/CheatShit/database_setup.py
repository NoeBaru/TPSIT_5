import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS Utenti (
    IdUtente INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL,
    TipoUtente TEXT NOT NULL CHECK (TipoUtente IN ('user', 'admin')),
    soldiCaricati INTEGER
)
''')

c.execute("INSERT INTO Utenti (Username, Password, TipoUtente, soldiCaricati) VALUES ('admin', 'admin123', 'admin', 1000)")
c.execute("INSERT INTO Utenti (Username, Password, TipoUtente, soldiCaricati) VALUES ('user1', 'user123', 'user', 500)")

conn.commit()
conn.close()
