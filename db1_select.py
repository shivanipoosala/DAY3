import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

s=conn.execute("select * from attendance2")
for i in s:
    print(i)