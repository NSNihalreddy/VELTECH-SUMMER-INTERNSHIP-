import pandas as pd

# Load dataset
df = pd.read_csv("ecommerce_customer_churn_large.csv")

# 1. Average Order Value by Subscription Type
print("Average Order Value by Subscription Type:")
print(df.groupby("subscription_type")["avg_order_value"].mean())

# 2. Average Total Orders by Gender
print("\nAverage Total Orders by Gender:")
print(df.groupby("gender")["total_orders"].mean())

# 3. Top 5 Customers by Total Orders
print("\nTop 5 Customers by Total Orders:")
print(df.nlargest(5, "total_orders")[["customer_id", "total_orders"]])
