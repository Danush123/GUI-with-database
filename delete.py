import cx_Oracle
conn=cx_Oracle.connect('SYSTEM/oracle@localhost')
print(conn)
cur=conn.cursor()
statement = 'delete from table1 where age<19'
cur.execute(statement)
conn.commit()
