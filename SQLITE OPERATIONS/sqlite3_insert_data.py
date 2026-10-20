import sqlite3
conn=sqlite3.connect('macfast.db')
print("Opened database")
while 1:
    rollno=input("enter rollno(enter 0 for exit):")
    if int(rollno)==0:
        break
    name=input("Enter name: ")
    mark=input("Enter mark: ")
    sql="insert into student values(%s,'%s',%s)\n"%(rollno,name,mark)
    print(sql)
    conn.execute(sql)
    conn.commit()
    print("\nRecords inserted")
conn.close()
