# Introduction

SQLite3 is a lightweight, serverless relational database management system (RDBMS) that can be easily embedded into Python applications. This documentation provides a guide on how to set up SQLite3 with Python and covers basic commands to interact with databases.

# Prerequisites

Python installed (version 3.x recommended)
Basic understanding of Python programming
Setup

1. Installing SQLite3
   Linux: SQLite3 is usually pre-installed. If not, use your package manager (e.g., apt, yum) to install sqlite3.

bash
Copy code
sudo apt-get install sqlite3
Windows: SQLite3 binaries are available for download from SQLite official website. Ensure to download the command-line shell and tools package.

2. Installing SQLite3 Python module
   SQLite3 comes pre-installed with Python, so usually, there's no need for additional installation. However, if necessary, you can install it via pip:

bash
Copy code
pip install db-sqlite3
Using SQLite3 with Python
Basic Commands and Operations

1. Connecting to a Database
   python
   Copy code
   import sqlite3

# Connect to SQLite database (creates if not exists)

conn = sqlite3.connect('example.db')

# Create a cursor object using the cursor() method

cursor = conn.cursor() 2. Creating Tables
python
Copy code

# Create a table

cursor.execute('''CREATE TABLE IF NOT EXISTS users
(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Save (commit) the changes

conn.commit() 3. Inserting Data
python
Copy code

# Insert data into table

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))
conn.commit() 4. Querying Data
python
Copy code

# Selecting data

cursor.execute("SELECT \* FROM users")
rows = cursor.fetchall()

for row in rows:
print(row) 5. Updating Data
python
Copy code

# Update data

cursor.execute("UPDATE users SET age = 26 WHERE name = 'Bob'")
conn.commit() 6. Deleting Data
python
Copy code

# Delete data

cursor.execute("DELETE FROM users WHERE name = 'Alice'")
conn.commit() 7. Closing the Connection
python
Copy code

# Close the cursor and connection

cursor.close()
conn.close()
