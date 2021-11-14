import sqlite3
import os
# conn = sqlite3.connect('./app.db')
# conn.execute('''CREATE TABLE IF NOT EXISTS Photos (
#          ID INT PRIMARY KEY     NOT NULL,
#          PATH           TEXT    NOT NULL,
#          LIKES            INT     NOT NULL,
#          DISLIKES        INT    NOT NULL
#          );''')
# conn.commit()
# conn.close()
# conn = sqlite3.connect('./app.db')

# i = 0
# for file in os.listdir('./static/photos'):
#     i+=1
#     conn.execute("INSERT INTO Photos \
#         VALUES({}, '{}', 0, 0)".format(i,file))
# conn.commit()
# conn.close()
conn = sqlite3.connect("app.db")
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()
likes = c.execute('SELECT likes FROM Photos').fetchall()
print(likes)