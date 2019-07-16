import cx_Oracle
conn=cx_Oracle.connect('SYSTEM/oracle@localhost')
cur=conn.cursor()
statement='update table1 set age=20 where age<20'
cur.execute(statement)
conn.commit()
