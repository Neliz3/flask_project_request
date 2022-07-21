import sqlite3


def create_db():
    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    # Create table
    cur.execute('''CREATE TABLE IF NOT EXISTS phones
                   (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   value VARCHAR(20))''')
    con.close()


def executing(search_data, sql, sms):
    con = sqlite3.connect('phones.db')
    cur = con.cursor()
    sql_search = f"""SELECT value FROM phones WHERE value='{search_data}'"""
    try:
        cur.execute(sql_search)
        result = cur.fetchall()

        # Exception. Does number_del exist in database?
        if not result:
            return f"'{search_data}' does not exist in database"
        else:
            cur.execute(sql)
            return sms
    finally:
        con.commit()
        con.close()
