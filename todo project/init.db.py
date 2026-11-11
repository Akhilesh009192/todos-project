import sqlite3

conn = sqlite3.connect("todos.db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
)
"""
)

seed = ["Learn Flask", "Learn SQL", "Build a project"]

# Fix: Wrap task in a tuple (task,) so sqlite3 can unpack it correctly
for task in seed:
    cursor.execute("INSERT INTO todos (task) VALUES (?)", (task,))

conn.commit()
conn.close()

print("Database ready.")

