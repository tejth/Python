import sqlite3


# ------------------------*************************************************--------------------------
# using existing database  
# conn = sqlite3.connect(':memory:')




# -----------------------************************************************-------------------------------------------
# creating connection 
conn = sqlite3.connect('customer.db')


# ---------------------------------*****************************************------------------------------------------------
# creating database table  
# cursors in sqlite3 python are objects that act as a pointer to the result of a query
#sqlite has only 5 datatypes NULL,INTEGER,REAL,TEXT,BLOB(IMAGE,MP3...)
c =  conn.cursor()
# c.execute("""CREATE TABLE customers(
#     first_name text,
#     last_name text, 
#     email  text
# )""")



# ---------------------------********************************-----------------------------------------





# Inserting one record into the table
# c.execute("INSERT INTO customers VALUES ('tej','pal','tej32@gmail.com')")


# ---------------------------------******************************************-----------------------------------------
# Inserting many records into the table
# many_customer =[('Wes','Brown','wes@brown.com'),
#                 ('Steph','Kuewa','steph@kuewa.com'),
#                 ('meera','kushwah','mksh@gmail.com'),
#                 ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customer)



# ----------------------------------------------------*******************************_-----------------------------------------
#QUERY THE DATABASE
c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany(3)
# print(c.fetchall())  #returns a python list


# ---------------------------------------**************************************----------------------------------------------
#Format result
# print(c.fetchone()[0])
# items = c.fetchall()

# for item in items:
#     print(item[0] + " "+ item[1]+"|" + "\t" +item[2])


#---------------------------------------------***************************************-------------------------------------------



print("command executed successfully")
# commit out command  
conn.commit()


# close our connection   
conn.close()

