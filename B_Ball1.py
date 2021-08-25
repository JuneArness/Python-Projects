

import sqlite3

conn = sqlite3.connect('B_Ball.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_players( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_positions TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('B_Ball.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_players(col_fname, col_lname, col_position) VALUES (?,?,?)", \
                ('Micheal', 'Jordan', 'Point Guard'))
    cur.execute("INSERT INTO tbl_players(col_fname, col_lname, col_position) VALUES (?,?,?)", \
                ('Kobe', 'Bryant', 'Shooting Guard'))
    cur.execute("INSERT INTO tbl_players(col_fname, col_lname, col_position) VALUES (?,?,?)", \
                ('LeBron', 'James', 'Small Forward'))
    conn.commit()
conn.close()


conn = sqlite3.connect('B_Ball.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_lname,col_position FROM tbl_players WHERE col_fname = 'Jordan'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: ()\nLast Name:()\position:()".format(item[0],item[1],item[2])
    print(msg)
    
