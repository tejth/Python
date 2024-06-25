import sqlite3

conn = sqlite3.connect('customer.db')
c =  conn.cursor()

#Ordering
c.execute("SELECT rowid,* FROM customers ORDER BY rowid DESC " )

items = c.fetchall()
for item in items :
    print(item)
    

conn.commit()
conn.close()
