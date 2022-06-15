import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

query='''
 update attendance2 set name='SHIVANI' WHERE g_id=100
'''
conn.execute(query)

print(conn.total_changes)
conn.commit()
conn.close()