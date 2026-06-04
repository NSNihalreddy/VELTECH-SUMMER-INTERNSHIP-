import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("ecommerce_customer_churn_large.csv")

# Calculate Churn Rate by Subscription Type
churn_rate = df.groupby('subscription_type')['churn'].mean()

# Mean Churn Rate
mean_churn = churn_rate.mean()

# Create Bar Chart
plt.figure(figsize=(8, 5))

colors = ['skyblue', 'lightgreen', 'orange']

plt.bar(
    churn_rate.index,
    churn_rate.values,
    color=colors[:len(churn_rate)]
)

# Mean Line
plt.axhline(
    y=mean_churn,
    color='red',
    linestyle='--',
    label=f'Average Churn Rate ({mean_churn:.2f})'
)

# Labels and Title
plt.title('Churn Rate by Subscription Type')
plt.xlabel('Subscription Type')
plt.ylabel('Churn Rate')

# Legend
plt.legend()

plt.tight_layout()

# Save Chart
plt.savefig('custom_churn_chart.png')

# Display Chart
plt.show()

print("Task 2 Completed Successfully!")
print("File Generated: custom_churn_chart.png")
