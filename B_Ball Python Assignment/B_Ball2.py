

import sqlite3

conn = sqlite3.connect('B_Ball.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_players(\
        ID INTEGER PRIOMARY KEY AUTOINCRIMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_position TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('B_Ball.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_players(col_fname, col_lname, col_position) VALUES (?,?,?)",\
                ('Micheal', 'Jordan', 'Point Guard'))
    conn.commit()
conn.close()
