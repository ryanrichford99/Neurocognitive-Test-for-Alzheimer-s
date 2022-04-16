import mysql.connector


mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    port = "8080",
    password = "",
    database = "Alz_db",
    )

print(mydb)