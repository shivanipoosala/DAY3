import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')


query='''
      create table attendance2(g_id int primary key,name text not null,attendance int)
'''

conn.execute(query)