import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2001",
    database="testdatabase",
    auth_plugin='mysql_native_password'
)

my_cursor = db.cursor()
# my_cursor.execute(""" CREATE TABLE Test
#                 (name varchar(50) NOT NULL,
#                  created datetime NOT NULL,
#                  gender ENUM('M', 'F', 'O') NOT NULL,
#                  id int PRIMARY KEY NOT NULL AUTO_INCREMENT)
#                   """)

# my_cursor.execute("""INSERT INTO Test (name, created, gender)
#                     VALUES (%s, %s, %s)""", ("Alicia", datetime.now(), "F"))
# db.commit()

# my_cursor.execute("""  SELECT name, id, gender
#                        FROM Test
#                        WHERE gender = 'M'
#                        Order by id DESC""")
# for id in my_cursor:
#     print(id)

# my_cursor.execute(""" ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL """)
# my_cursor.execute("DESCRIBE Test")
# print(my_cursor.fetchall())

my_cursor.execute(""" ALTER TABLE Test CHANGE name first_name VARCHAR(50) """)
my_cursor.execute("DESCRIBE Test")

for x in my_cursor:
    print(x)