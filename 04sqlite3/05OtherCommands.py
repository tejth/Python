import sqlite3

conn = sqlite3.connect('customer.db')
c =  conn.cursor()
#AND/OR
# c.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'Br%' AND rowid=3 " )
#Limit
# c.execute("SELECT rowid,* FROM customers LIMIT 2 " )
#Drop
# c.execute("DROP TABLE customers" )

items = c.fetchall()
for item in items :
    print(item)
    

conn.commit()
conn.close()
