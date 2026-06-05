import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("DATA/ecommerce_customer_churn_large.csv")

# Encode categorical columns
df = pd.get_dummies(df, columns=["gender", "city", "subscription_type"], drop_first=True)

# Features and Target
X = df.drop("churn", axis=1)
y = df["churn"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save Model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

# Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(X.columns.tolist())

print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("model.pkl saved successfully!")