import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

query='''
    alter table attendance2 add column age int 
'''

conn.execute(query)
conn.commit()
conn.close()