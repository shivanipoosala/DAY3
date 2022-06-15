import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

str=conn.execute("pragma table_info('attendance2')")
print(str)
for i in str:
    print(i)