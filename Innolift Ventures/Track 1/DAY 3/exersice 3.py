import pandas as pd

# Load dataset
df = pd.read_csv("ecommerce_customer_churn_large.csv")

# Shape
print("Dataset Shape:")
print(df.shape)

# Column Names
print("\nColumn Names:")
print(df.columns.tolist())

# First 3 Rows
print("\nFirst 3 Rows:")
print(df.head(3))

# Last 3 Rows
print("\nLast 3 Rows:")
print(df.tail(3))

# Churn Count
print("\nCustomer Churn Count:")
print(df["churn"].value_counts())

# Churn Percentage
print("\nCustomer Churn Percentage:")
print(df["churn"].value_counts(normalize=True) * 100)
