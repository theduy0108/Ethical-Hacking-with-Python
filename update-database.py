import sqlite3 as sql

conn = sql.connect('customer.db')

c = conn.cursor()


# Update records
# c.execute(""" UPDATE customers SET last_name = "Phan"
#             WHERE rowid = 3
# """)
c.execute(""" DELETE from customers 
              WHERE  rowid = 6
                """)

conn.commit()


# Query the database
c.execute("""SELECT rowid, *
             FROM customers """)
# c.fetchone()
# c.fetchmany(3)

print(c.fetchall())

items = c.fetchall()
for item in items:
    print(item)


conn.commit()
conn.close()
# add comment for close data
