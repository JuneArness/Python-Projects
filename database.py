import sqlite3

import os.path

conn = sqlite3.connect('B_Ball.db')



fileList = ('information.docx', 'Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_highlights(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_points STRING)")
    conn.commit()

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_highlights (col_points) VALUES (?)", (x,))
            print(x)




