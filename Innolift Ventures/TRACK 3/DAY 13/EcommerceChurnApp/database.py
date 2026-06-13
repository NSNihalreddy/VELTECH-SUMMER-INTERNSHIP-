import sqlite3

conn = sqlite3.connect("churn.db")

conn.execute("""
DROP TABLE IF EXISTS customers
""")

conn.execute("""
CREATE TABLE customers(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

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
    confidence REAL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")