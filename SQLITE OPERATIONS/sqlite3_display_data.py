import sqlite3
conn=sqlite3.connect('macfast.db')
print('opened database')
print('displaying data')
print("\n............")
result=conn.execute("select * from student")
print("Rollno|Name|Marks")
print("\n............")
for i in result:
    print("%6s|%-15s|%3s"%(i[0],i[1],i[2]))
print("\n...........")
conn.close()
