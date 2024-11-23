import sqlite3

# Create database and table
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

# Create 'users' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Add sample users for testing
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('john', 'securepass')")
cursor.execute("INSERT INTO users (username, password) VALUES ('jane', 'mypassword')")

connection.commit()
connection.close()
print("Database setup complete!")
