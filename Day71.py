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
#INSERT INTO
sql="INSERT INTO cutomers (name, address) VALUES(%s, %s)"
#execute many
val=("John","Highway 21")
mycursor.execute(sql,val)
val=[('Peter','Valley 4'),
('Amy','Sky st 331'),
('Betty','One way 98'),
('Ben','Sideway 20')]
mycursor.executemany(sql,val)
print(mycursor.rowcount,"record inserted.")
#execute one row
val=("shamaah","Highway 21")
mycursor.execute(sql,val)
mydb.commit()
print("1 record add , ID:",mycursor.lastrowid)
#select all
mycursor.execute("SELECT * FROM cutomers")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)
#select columns 
print("---select column---")
mycursor.execute("SELECT name, address FROM cutomers")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)
#first row 
print("---one row---")   
mycursor.execute("SELECT * FROM cutomers")
myresult=mycursor.fetchone()
print(myresult)
#where
sql="SELECT * FROM cutomers  WHERE name='shamaah'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
  print(x)
print("----------------------------")
sql2="SELECT * FROM cutomers  WHERE address Like '%way%'"
mycursor.execute(sql2)
myresult=mycursor.fetchall()
for x in myresult:
  print(x)  


