import os
import mysql.connector

db = mysql.connector.connect(
  host=os.getenv("MYSQL_IP"),
  user=os.getenv("MYSQL_USER"),
  password=os.getenv("MYSQL_PASSWORD"),
  database="responses"
)

cursor = db.cursor()

cursor.execute("CREATE TABLE bad (id INT AUTO_INCREMENT PRIMARY KEY, prompt TEXT(255), completion LONGTEXT)")
cursor.execute("CREATE TABLE good (id INT AUTO_INCREMENT PRIMARY KEY, prompt TEXT(255), completion LONGTEXT)")

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x) 