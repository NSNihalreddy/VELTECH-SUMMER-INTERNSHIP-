import pickle
import pandas as pd

# Load Saved Model
with open("churn_model.pkl", "rb") as file:
    model = pickle.load(file)

# 3 New Customers
customers = pd.DataFrame([
    [25, 12, 400, 20, 10, 1],
    [45, 3, 150, 5, 60, 4],
    [30, 24, 700, 40, 5, 0]
], columns=[
    'age',
    'tenure_months',
    'avg_order_value',
    'total_orders',
    'last_purchase_days_ago',
    'support_tickets'
])

# Predictions
predictions = model.predict(customers)

print("\nCustomer Churn Predictions")
print("-" * 30)

for i, pred in enumerate(predictions, start=1):
    result = "Will Churn" if pred == 1 else "Will Stay"
    print(f"Customer {i}: {result}")
