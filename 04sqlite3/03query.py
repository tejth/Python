import sqlite3

conn = sqlite3.connect('customer.db')
c =  conn.cursor()



#primary key
# c.execute("SELECT * FROM customers WHERE last_name ='Elder' " )
# c.execute("SELECT * FROM customers WHERE last_name Like 'pa%' " )

#update records
# c.execute("""
#           UPDATE customers SET first_name='Marry' ss
#           WHERE rowid=5
#           """)
# c.execute("SELECT rowid,* FROM customers " )


#Deleting Records
# c.execute("DELETE from customers WHERE rowid=5")
# c.execute("SELECT rowid,* FROM customers " )


items = c.fetchall()
for item in items :
    print(item)
    
    

conn.commit()
conn.close()
