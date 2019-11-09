import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  #create db here
  database="mydatabase"
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM cutomers ORDER BY name")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)
print("--------------------")  
mycursor.execute("SELECT * FROM cutomers ORDER BY name DESC")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)  

sql="DELETE FROM cutomers WHERE id=3 "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"reord(s) deleted")
#delete table
sql="DROP TABLE IF EXISTS cutomers"
mycursor.execute(sql)
