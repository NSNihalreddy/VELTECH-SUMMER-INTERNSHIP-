import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load Dataset
df = pd.read_csv("ecommerce_customer_churn_large.csv")

# Features (X)
X = df[
    [
        'age',
        'tenure_months',
        'avg_order_value',
        'total_orders',
        'last_purchase_days_ago',
        'support_tickets'
    ]
]

# Target (y)
y = df['churn']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = LogisticRegression(max_iter=1000)

# Train Model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("=" * 50)
print("CUSTOMER CHURN PREDICTION MODEL")
print("=" * 50)

print(f"Accuracy  : {accuracy:.2%}")
print(f"Precision : {precision:.2%}")
print(f"Recall    : {recall:.2%}")
print(f"F1 Score  : {f1:.2%}")

# Predict a New Customer
new_customer = [[
    30,    # age
    12,    # tenure_months
    500,   # avg_order_value
    25,    # total_orders
    15,    # last_purchase_days_ago
    2      # support_tickets
]]

prediction = model.predict(new_customer)

print("\nNew Customer Prediction:")

if prediction[0] == 1:
    print("Customer is likely to CHURN")
else:
    print("Customer is likely to STAY")

print("=" * 50)
print("Task 4 Completed Successfully!")
