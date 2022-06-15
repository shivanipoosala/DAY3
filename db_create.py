import sqlite3
conn=sqlite3.connect('bootcamp.db')

query = '''
       create table stud(g_id int ,name text ,branch text )
        '''
conn.execute(query)
conn.commit()
conn.close()