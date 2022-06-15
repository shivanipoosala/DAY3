import sqlite3
conn=sqlite3.connect('bootcamp.db')

conn.execute("insert into stud values(221,'shivani','csai')")
conn.execute("insert into stud values(220,'shiva','cse')")

conn.commit()
conn.close()