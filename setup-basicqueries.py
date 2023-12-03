import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2001",
    database="testdatabase"
)

my_cursor = db.cursor()

