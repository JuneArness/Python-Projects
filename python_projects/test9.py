

import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
        ID INTEGER PRIOMARY KEY AUTOINCRIMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_paersons(col_fname, col_lname, col_email) VALUES (?,?,?)",\
                ('Bob', 'Smith', 'bsmith@gmail.com'))
    conn.commit()
conn.close()
