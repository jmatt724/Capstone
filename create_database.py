import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="$Ilovechess6969", database="capstone"
                               , auth_plugin="mysql_native_password")

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)