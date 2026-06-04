import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load Dataset
df = pd.read_csv("ecommerce_customer_churn_large.csv")

# Features
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

# Target
y = df['churn']

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

# Save Model
with open("churn_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully as churn_model.pkl")
