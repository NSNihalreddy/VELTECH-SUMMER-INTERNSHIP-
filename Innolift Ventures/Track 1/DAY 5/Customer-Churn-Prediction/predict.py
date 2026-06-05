import pickle
import pandas as pd

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Sample customers
sample_data = pd.DataFrame({
    'customer_id': [300001, 300002, 300003],
    'age': [25, 45, 60],
    'tenure_months': [12, 48, 90],
    'avg_order_value': [3000, 6000, 8000],
    'total_orders': [50, 200, 400],
    'last_purchase_days_ago': [30, 120, 400],
    'support_tickets': [2, 10, 30],
    'gender_Male': [1, 0, 1],
    'city_Chennai': [0, 1, 0],
    'city_Delhi': [1, 0, 0],
    'city_Hyderabad': [0, 0, 1],
    'city_Kolkata': [0, 0, 0],
    'city_Mumbai': [0, 0, 0],
    'city_Pune': [0, 0, 0],
    'subscription_type_Gold': [1, 0, 0],
    'subscription_type_Platinum': [0, 1, 0],
    'subscription_type_Silver': [0, 0, 1]
})

predictions = model.predict(sample_data)

print("Customer Churn Predictions")
print("-" * 30)

for i, pred in enumerate(predictions, start=1):
    if pred == 1:
        print(f"Customer {i}: Likely to Churn")
    else:
        print(f"Customer {i}: Likely to Stay")