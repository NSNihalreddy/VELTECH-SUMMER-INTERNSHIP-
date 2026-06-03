import pandas as pd

# Load dataset
df = pd.read_csv("ecommerce_customer_churn_large.csv")

# 1. Dataset Shape
print("Dataset Shape:")
print(df.shape)

# 2. Dataset Information
print("\nDataset Information:")
print(df.info())

# 3. Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# 4. Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Churn Distribution
print("\nChurn Distribution:")
print(df["churn"].value_counts())

# 6. Gender Distribution
print("\nGender Distribution:")
print(df["gender"].value_counts())

# 7. Subscription Type Distribution
print("\nSubscription Type Distribution:")
print(df["subscription_type"].value_counts())

# 8. Average Order Value
print("\nAverage Order Value:")
print(df["avg_order_value"].mean())

# 9. Average Total Orders
print("\nAverage Total Orders:")
print(df["total_orders"].mean())
