import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

conn.execute("insert into attendance2 values(105,'shivani',98,'cse')")
conn.execute("insert into attendance2 values(106,'rani',88,'ece')")
conn.execute("insert into attendance2 values(107,'shiva',78,'eee')")
conn.execute("insert into attendance2 values(108,'anu',88,'csai')")

conn.commit()
conn.close()