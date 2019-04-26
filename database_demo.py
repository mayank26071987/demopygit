import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="mayank"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)