import sqlite3 as sql


def show_all():
    conn = sql.connect('customer.db')
    c = conn.cursor()
    c.execute("""
        SELECT rowid, *
        FROM customers
    """)

    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()


def add_one(first, last, email):
    conn = sql.connect('customer.db')
    c = conn.cursor()
    c.execute("""
         INSERT INTO customers
         VALUES (?, ?, ?)
        """, (first, last, email))
    conn.commit()
    conn.close()


def delete_one(id):
    conn = sql.connect('customer.db')
    c = conn.cursor()
    c.execute(""" DELETE from customers 
                  WHERE rowid = (?) """, id)
    conn.commit()
    conn.close()


def add_many_records(list_record):
    conn = sql.connect('customer.db')
    c = conn.cursor()

    c.executemany("""INSERT INTO customers VALUES (?,?,?)""", list_record)
    conn.commit()
    conn.close()


