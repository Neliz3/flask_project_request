import sqlite3


# Creating database
def create_db():
    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    # Create table
    cur.execute('''CREATE TABLE IF NOT EXISTS phones
                   (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   value VARCHAR(20))''')
    con.close()


# Connecting to database and error checking
def executing(search_data, sql, sms):
    con = sqlite3.connect('phones.db')
    cur = con.cursor()
    sql_search = f"""SELECT value FROM phones WHERE value='{search_data}'"""
    try:
        cur.execute(sql_search)
        result = cur.fetchall()

        # Exception. Does search_data exist in database?
        if not result:
            return f"'{search_data}' does not exist in database"
        else:
            cur.execute(sql)
            return sms
    finally:
        con.commit()
        con.close()
