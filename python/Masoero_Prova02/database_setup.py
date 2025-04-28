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

c.execute('''
CREATE TABLE IF NOT EXISTS Prodotti (
    Idprodotto INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Peso TEXT NOT NULL,
    Costo INTEGER
)
''')

c.execute("INSERT INTO Prodotti (Nome, Peso, Costo) VALUES ('Anguria', '6kg', 6)")
c.execute("INSERT INTO Prodotti (Nome, Peso, Costo) VALUES ('Mela', '200g', 1)")
c.execute("INSERT INTO Prodotti (Nome, Peso, Costo) VALUES ('Banana', '250g', 1)")
c.execute("INSERT INTO Prodotti (Nome, Peso, Costo) VALUES ('Pera', '180g', 1)")
c.execute("INSERT INTO Prodotti (Nome, Peso, Costo) VALUES ('Ananas', '2kg', 4)")
c.execute("INSERT INTO Prodotti (Nome, Peso, Costo) VALUES ('Melone', '3kg', 3)")
c.execute("INSERT INTO Prodotti (Nome, Peso, Costo) VALUES ('Uva', '500g', 2)")
c.execute("INSERT INTO Prodotti (Nome, Peso, Costo) VALUES ('Fragole', '300g', 3)")
c.execute("INSERT INTO Prodotti (Nome, Peso, Costo) VALUES ('Pesca', '220g', 1)")
c.execute("INSERT INTO Prodotti (Nome, Peso, Costo) VALUES ('Ciliegie', '400g', 3)")

conn.commit()
conn.close()
