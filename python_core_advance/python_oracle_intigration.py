# connecting python with oracle  and reading the data
import cx_Oracle
con = cx_Oracle.connect('hr/hr@orclpdb')
cursor=con.cursor()
res=cursor.execute("select * from emp1")
res=cursor.fetchone()
print(res)

cursor.close()
con.close()
