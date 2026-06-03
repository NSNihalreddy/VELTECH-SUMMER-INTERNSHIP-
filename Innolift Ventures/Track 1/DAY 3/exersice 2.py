import pandas as pd

# Manually create data for 5 students
data = {
    "name": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran"],
    "age": [20, 21, 19, 22, 20],
    "city": ["Hyderabad", "Vijayawada", "Chennai", "Bangalore", "Mumbai"],
    "marks": [85, 45, 72, 38, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print head, shape, and dtypes
print("Head:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

# Add result column
df["result"] = df["marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("\nDataFrame with Result Column:")
print(df)
