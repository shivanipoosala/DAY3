import sqlite3
conn=sqlite3.connect('bootcamp.db')

str=conn.execute("pragma table_info('stud')")
print(str)
for i in str:
    print(i)