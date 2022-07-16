import sqlite3

con = sqlite3.connect('phones.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS phones
               (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               value INTEGER NOT NULL)''')
con.close()
