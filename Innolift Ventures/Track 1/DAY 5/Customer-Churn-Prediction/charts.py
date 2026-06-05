import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("DATA/ecommerce_customer_churn_large.csv")

# Chart 1: Churn Distribution
plt.figure(figsize=(6,4))
df["churn"].value_counts().plot(kind="bar")
plt.title("Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Count")
plt.savefig("churn_distribution.png")
plt.close()

# Chart 2: Average Order Value vs Churn
plt.figure(figsize=(6,4))
df.groupby("churn")["avg_order_value"].mean().plot(kind="bar")
plt.title("Average Order Value by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Order Value")
plt.savefig("feature_vs_churn.png")
plt.close()

# Chart 3: Correlation Heatmap
plt.figure(figsize=(8,6))
corr = df.select_dtypes(include=["int64","float64"]).corr()
plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

print("All charts saved successfully!")