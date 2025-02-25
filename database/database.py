import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create a table to store user data
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    favorite_author TEXT NOT NULL,
    favorite_language TEXT NOT NULL,
    genres TEXT NOT NULL
)
''')

# Commit and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
