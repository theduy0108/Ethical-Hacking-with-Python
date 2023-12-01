import sqlite3 as sql

conn = sql.connect('customer.db')

c = conn.cursor()


# Update records

# Query the database
c.execute("""SELECT *
             FROM customers
             WHERE first_name = "Alicia" """)
# c.fetchone()
# c.fetchmany(3)

# print(c.fetchall())

items = c.fetchall()
for item in items:
    print(item)


conn.commit()
conn.close()
# add comment for close data
