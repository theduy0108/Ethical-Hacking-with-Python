import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2001",
    database="testdatabase",
    auth_plugin='mysql_native_password'
)

users = [("tim", "techwithtim"),
         ("duy", "cybersecurity"),
         ("alicia", "foodscience_qc")]

user_scores = [(45, 100),
               (30, 200),
               (46, 124)]

my_cursor = db.cursor()

Q1 = """ CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT , 
                             name VARCHAR(50),
                             passwd VARCHAR(50)) """
Q2 = """ CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userID) REFERENCES Users(id), 
                              game1 int DEFAULT 0,
                              game2 int DEFAULT 0) """
# my_cursor.execute(Q1)
# my_cursor.execute(Q2)

# my_cursor.execute("DESCRIBE Users")
# for data in my_cursor:
#     print(data)
#
# my_cursor.execute("DESCRIBE Scores")
# for data in my_cursor:
#     print(data)

# my_cursor.executemany(""" INSERT INTO Users (name, passwd) VALUES (%s, %s) """, users)
# db.commit()

# my_cursor.execute(""" SELECT id from Users """)
# user_id_from_user_table = [ids[0] for ids in my_cursor]
# new_scores = []
# for index, scores in enumerate(user_scores):
#     scores = list(scores)
#     scores.insert(0, user_id_from_user_table[index])
#     new_scores.append(tuple(scores))
#
# my_cursor.executemany(""" INSERT INTO Scores (userId, game1, game2) VALUES (%s, %s, %s) """, new_scores)
# db.commit()

my_cursor.execute("SELECT * FROM Scores")
for rows in my_cursor:
    print(rows)
