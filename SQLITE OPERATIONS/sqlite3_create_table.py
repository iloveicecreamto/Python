import sqlite3
conn=sqlite3.connect('macfast.db')
print("Opened database")
sql="create table student(rollno int(3),name varchar(30),mark int(3))"
conn.execute(sql)
print("Table created")
conn.close()
