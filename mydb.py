# URUTAN KERJA

# install mysql on your computer
# install mysql-connector-python library

import  mysql.connector

database  = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
)

# prepare  a cursor object using cursor() method
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE medio")

print("All Done!")


