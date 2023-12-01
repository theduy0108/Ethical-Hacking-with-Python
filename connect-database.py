import sqlite3 as sql

# conn = sql.connect(':memory:') save the database

conn = sql.connect('customer.db')

# create a cursor
c = conn.cursor()

# Create a Table
"""
5 datatypes in SQLlite
NULL
INTERGER
REAL
TEXT
BLOB: store data like image or mp3 file
"""
# c.execute(""" CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
#     ) """)

# c.execute("""INSERT INTO customers VALUES (
#             'TD', 'Young', 'duyphan01082001@gmail.com'
# )""") # insert one columns

many_users = [('West', 'Brown', 'westbrown@unsa.com'),
              ('Adelaide', 'Airport', 'Adelaide-airport@gmail.com'),
              ('Alicia', 'Nguyen', 'UniAdel@uniadel.com')]
c.executemany("""INSERT INTO customers VALUES (?,?,?)""", many_users)


# Commit our command
conn.commit()
# Close our connection
conn.close()
