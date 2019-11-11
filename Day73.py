import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)
mycursor=mydb.cursor()
sql="Update cutomers SET address='Canyon 123' WHERE address='Highway 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")
mycursor.execute("SELECT * FROM cutomers LIMIT 3")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)
print("------------------------")  
#return # of record start from spasicf record 
mycursor.execute("SELECT * FROM cutomers LIMIT 2 OFFSET 3")
myresult=mycursor.fetchall()
for x in myresult:
  print(x) 
print("-------------------------")  
sql="SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    INNER JOIN products ON users.fav = products.id "
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
  print(x)
print("-------------------------") 
sql="SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    LEFT JOIN products ON users.fav = products.id "
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
  print(x)
print("-------------------------")  
sql="SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    RIGHT JOIN products ON users.fav = products.id "
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
  print(x)