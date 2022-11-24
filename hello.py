import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shubham",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE university")
