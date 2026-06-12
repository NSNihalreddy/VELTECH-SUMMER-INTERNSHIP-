import sqlite3

conn = sqlite3.connect("churn.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tenure REAL,
    warehouse_to_home REAL,
    devices_registered INTEGER,
    satisfaction_score INTEGER,
    order_count INTEGER,
    cashback_amount REAL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")