import sqlite3

conn = sqlite3.connect("churn.db")



conn.execute("""
CREATE TABLE IF NOT EXISTS customers(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    customer_id INTEGER,
    age INTEGER,
    tenure_months INTEGER,

    avg_order_value REAL,
    total_orders INTEGER,

    last_purchase_days_ago INTEGER,
    support_tickets INTEGER,

    gender TEXT,
    city TEXT,
    subscription_type TEXT,

    prediction TEXT,
    confidence REAL,
    risk_level TEXT,

    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")
conn.commit()
conn.close()

print("Database Created Successfully")
import sqlite3

conn = sqlite3.connect("churn.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()
conn.close()

print("Users table created successfully")
