#Python sqlite3 example
#structured query language
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# Insert data into the table
c.execute('INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)', ('John Doe', 'johndoe@example.com'))
c.execute('INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)', ('Jane Doe', 'janedoe@example.com'))
c.execute('INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)', ('David Swan', 'dswan@example.com'))
c.execute('INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)', ('Bobb Swan', 'bbbbswan@example.com'))
# Commit the changes
conn.commit()

# Query the table
c.execute('SELECT * FROM users')
for row in c.fetchall():
    print(row)

# Close the connection
conn.close()