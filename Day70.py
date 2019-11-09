import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  #create db here
  database="mydatabase"
)
print(mydb)
mycursor=mydb.cursor()
#To create db
mycursor.execute("CREATE DATABASE mydatabase")
#To show all data in server
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
#To create table
mycursor.execute("CREATE TABLE cutomers(name VARCHAR(255), address VARCHAR(255) )")
#To Modify table
mycursor.execute("ALTER TABLE cutomers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x) 

