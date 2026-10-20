import sqlite3
conn=sqlite3.connect('macfast.db')
print("opened database")
print("Deleting data")
print("\n..........")
result=conn.execute('''DELETE from student where rollno=3;''')
print("Rollno|Name|Marks")
print("\n..........")
data=conn.execute("select * from student")
for i in data:
    print(i)
print("\n.........")
conn.commit()
conn.close()
