import mysql.connector
import os
print("****1****")
print("-----Before Edit------")
f=open("Text_1.txt","r")
print(f.read())
f.close()
f=open("Text_1.txt","a")
f.write(" The best way we learn anything is by practice and exercise questions")
f.close()
print("-----After Edit------")
f=open("Text_1.txt","r")
print(f.read())
f.close()
print("****2****")
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="MyEmployee "
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE MyEmployee")
mycursor.execute("CREATE TABLE Employee (FirstName VARCHAR(255),LastName VARCHAR(255), Age INT ,Gender VARCHAR(255),Salary INT )")
mycursor.execute("INSERT INTO Employee (FirstName,LastName,Age,Gender,Salary) VALUES('Ahmed','Ali',30,'Male',10000)")
mycursor.execute("INSERT INTO Employee (FirstName,LastName,Age,Gender,Salary) VALUES('Khalid','Muhammad',34,'Male',7000)")
mycursor.execute("INSERT INTO Employee (FirstName,LastName,Age,Gender,Salary) VALUES('Norah','Saleh',29,'Female',7000)")
mydb.commit()
print(mycursor.rowcount,"records")  
print("----show all table----")
mycursor.execute("SELECT * FROM Employee")
myresult=mycursor.fetchall()
for x in myresult:
  print(x) 
print("----show first name ,gender and salary from table----")
mycursor.execute("SELECT FirstName,Gender,Salary FROM Employee")
myresult=mycursor.fetchall()
for x in myresult:
  print(x) 
print("----show all table with orderby first name----")
mycursor.execute("SELECT * FROM Employee ORDER BY FirstName DESC")
myresult=mycursor.fetchall()
for x in myresult:
  print(x) 
print("----delete row where age =34----")

#mycursor.execute("DELETE FROM Employee WHERE Age = 34")
#mydb.commit()

mycursor.execute("SELECT * FROM Employee")
myresult=mycursor.fetchall()
for x in myresult:
  print(x) 