import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("ecommerce_customer_churn_large.csv")

# Features to Compare
features = [
    'age',
    'tenure_months',
    'avg_order_value',
    'total_orders',
    'last_purchase_days_ago',
    'support_tickets'
]

# Target
y = df['churn']

print("=" * 60)
print("FEATURE COMPARISON USING LOGISTIC REGRESSION")
print("=" * 60)

results = []

for feature in features:

    # Use one feature at a time
    X = df[[feature]]

    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Train Model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)

    results.append([feature, accuracy])

    print(f"{feature:<25} Accuracy = {accuracy:.2%}")

# Find Best Feature
best_feature = max(results, key=lambda x: x[1])

print("\n" + "=" * 60)
print(f"Best Feature : {best_feature[0]}")
print(f"Best Accuracy: {best_feature[1]:.2%}")
print("=" * 60)

print("Task 5 Completed Successfully!")
