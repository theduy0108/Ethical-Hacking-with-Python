import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2001",
    database="testdatabase"
)

my_cursor = db.cursor()

# my_cursor.execute(""" CREATE TABLE Person
#                       (name VARCHAR(50),
#                        age  smallint  UNSIGNED,
#                        personID int PRIMARY KEY AUTO_INCREMENT) """)

# my_cursor.execute("DESCRIBE Person")
# for x in my_cursor:
#     print(x)

# my_cursor.execute("""INSERT INTO Person (name, age) VALUES (%s, %s)""",
#                   ("Joe", 19))
# db.commit()

my_cursor.execute("SELECT * FROM Person")
for x in my_cursor:
    print(x)