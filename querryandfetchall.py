import sqlite3 as sql

conn = sql.connect('customer.db')

c = conn.cursor()

c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany(3)

#print(c.fetchall())

items = c.fetchall()
# format the result
for item in items:
    print(item[0] + " | " + item[1] + " | " + item[2])

conn.commit()
conn.close()
# add comment for close data
