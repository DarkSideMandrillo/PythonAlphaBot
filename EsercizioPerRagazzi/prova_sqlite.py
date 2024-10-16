import sqlite3

# Connessione al database
conn = sqlite3.connect('mio_database.db')
cur = conn.cursor()

cur.execute('''''')
conn.commit()
variabile_in_stampa = cur.fetchall()
#conn.close()

# Crea la tabella con il vincolo UNIQUE
cur.execute('''
    CREATE TABLE IF NOT EXISTS studenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cognome TEXT NOT NULL,
        eta INTEGER NOT NULL,
        UNIQUE(nome, cognome)
    )
''')

# Inserisce dati solo se non esistono già
cur.execute('''
    INSERT OR IGNORE INTO studenti (nome, cognome, eta)
    VALUES ('Mario', 'Rossi', 18)
''')

# Inserisce un altro record
cur.execute('''
    INSERT OR IGNORE INTO studenti (nome, cognome, eta)
    VALUES ('Luca', 'Bianchi', 19)
''')

conn.commit()

# Recupera i dati
cur.execute('SELECT * FROM studenti')
studenti = cur.fetchall()

# Mostra i risultati
for studente in studenti:
    print(studente)

# Chiudi la connessione
conn.close()
