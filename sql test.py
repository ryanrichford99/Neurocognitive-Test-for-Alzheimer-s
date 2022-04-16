import mysqlx.connection
import mysql.connector

mydb= mysqlx.connection.connect(
    host = "localhost",
    user = "root",
    port = "8080",
    password = "",
    database = "Alz_db"
)

mycursor = mydb.cursor("select * from student")

for i in mycursor:
    print(i)
