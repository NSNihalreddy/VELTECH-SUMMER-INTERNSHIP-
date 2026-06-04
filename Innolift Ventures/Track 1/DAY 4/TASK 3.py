import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

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

# Different test sizes
test_sizes = [0.1, 0.2, 0.3]

for size in test_sizes:

    print("\n" + "=" * 40)
    print(f"Test Size = {size}")
    print("=" * 40)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=size,
        random_state=42
    )

    # Train Model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Training Samples : {len(X_train)}")
    print(f"Testing Samples  : {len(X_test)}")
    print(f"Accuracy         : {accuracy:.2%}")

print("\nTask 3 Completed Successfully!")
