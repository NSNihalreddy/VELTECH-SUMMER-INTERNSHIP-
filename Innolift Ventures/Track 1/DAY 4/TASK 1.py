import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("ecommerce_customer_churn_large.csv")

# ==========================================
# 1. BAR CHART
# Average Order Value by Subscription Type
# ==========================================
plt.figure(figsize=(8, 5))

df.groupby('subscription_type')['avg_order_value'].mean().plot(
    kind='bar'
)

plt.title('Average Order Value by Subscription Type')
plt.xlabel('Subscription Type')
plt.ylabel('Average Order Value')
plt.tight_layout()

plt.savefig('avg_order_value_by_subscription.png')
plt.show()

# ==========================================
# 2. SCATTER PLOT
# Tenure vs Total Orders
# ==========================================
plt.figure(figsize=(8, 5))

plt.scatter(
    df['tenure_months'],
    df['total_orders']
)

plt.title('Tenure vs Total Orders')
plt.xlabel('Tenure (Months)')
plt.ylabel('Total Orders')
plt.tight_layout()

plt.savefig('tenure_vs_orders.png')
plt.show()

# ==========================================
# 3. HISTOGRAM
# Age Distribution
# ==========================================
plt.figure(figsize=(8, 5))

plt.hist(
    df['age'],
    bins=10
)

plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()

plt.savefig('age_distribution.png')
plt.show()

# ==========================================
# 4. LINE CHART
# Average Customer Metrics
# ==========================================
metrics = [
    'avg_order_value',
    'total_orders',
    'support_tickets'
]

avg_values = [
    df['avg_order_value'].mean(),
    df['total_orders'].mean(),
    df['support_tickets'].mean()
]

plt.figure(figsize=(8, 5))

plt.plot(
    metrics,
    avg_values,
    marker='o'
)

plt.title('Average Customer Metrics')
plt.xlabel('Metrics')
plt.ylabel('Average Value')
plt.tight_layout()

plt.savefig('customer_metrics_trend.png')
plt.show()

print("===================================")
print("Task 1 Completed Successfully")
print("Generated PNG Files:")
print("1. avg_order_value_by_subscription.png")
print("2. tenure_vs_orders.png")
print("3. age_distribution.png")
print("4. customer_metrics_trend.png")
print("===================================")
