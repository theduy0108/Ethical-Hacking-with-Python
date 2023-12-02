import sqlite3 as sql

conn = sql.connect('customer.db')

c = conn.cursor()


# Update records
c.execute(""" SELECT rowid, * 
              FROM customers
              WHERE last_name LIKE 'P%' or first_name LIKE '%D%'
              LIMIT 10
""")
print(c.fetchall())
# c.fetchone()
# c.fetchmany(3)

items = c.fetchall()
for item in items:
    print(item)

conn.commit()
conn.close()

# Drop table
# c.execute(""" DROP TABLE customers
# """)
# c.commit()
#
