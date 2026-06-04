import pandas as pd
import matplotlib.pyplot as plt
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

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Scatter Plot
plt.figure(figsize=(8, 5))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.6
)

# Perfect Prediction Line
plt.plot(
    [0, 1],
    [0, 1],
    'r--',
    linewidth=2,
    label='Perfect Prediction'
)

plt.title('Actual vs Predicted Churn')
plt.xlabel('Actual Churn')
plt.ylabel('Predicted Churn')
plt.legend()

plt.tight_layout()

# Save Plot
plt.savefig('predict_vs_actual.png')

plt.show()

print("Task 6 Completed Successfully!")
print("File Generated: predict_vs_actual.png")
