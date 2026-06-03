import pandas as pd

# Load dataset
df = pd.read_csv("ecommerce_customer_churn_large.csv")

# Check missing values
print("Missing Values Before Cleaning:")
print(df.isnull().sum())

# Fill numeric columns with mean
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# Fill text columns with 'Unknown'
text_cols = df.select_dtypes(include=['object']).columns

for col in text_cols:
    df[col] = df[col].fillna("Unknown")

# Verify no missing values remain
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Check if dataset is clean
print("\nTotal Missing Values Remaining:")
print(df.isnull().sum().sum())
