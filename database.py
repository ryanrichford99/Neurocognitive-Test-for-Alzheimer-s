import pymysql
import mysql.connector

connection = pymysql.connect(host='localhost', port=8080, user='root', passwd='', database='battery001' )
cursor = connection.cursor()

connect_timeout = 600;
connect_timeout = 700;

retrieve = "Select * from data;"

cursor.execute(retrieve)
rows = cursor.fetchall()
for row in rows:
   print(row)


#commiting the connection then closing it.
connection.commit()
connection.close()




