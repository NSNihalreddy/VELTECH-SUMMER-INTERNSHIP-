import sqlite3

conn = sqlite3.connect('students.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    rollno TEXT,
    department TEXT,
    year TEXT,
    email TEXT,
    phone TEXT,
    gender TEXT,
    address TEXT
)
''')

conn.commit()
conn.close()

print("Database Created Successfully")