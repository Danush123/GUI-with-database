import cx_Oracle
conn=cx_Oracle.connect('SYSTEM/oracle@localhost')
print(conn)
cur=conn.cursor()
statement = 'insert into table1(name, age) values (:1, :2)'
cur.execute(statement, ('Sand', 3,))
conn.commit()
