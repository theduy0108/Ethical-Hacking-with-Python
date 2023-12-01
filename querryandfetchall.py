import sqlite3 as sql

conn = sql.connect('customer.db')

c = conn.cursor()

c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany(3)

print(c.fetchall())
c.commit()
c.close()

