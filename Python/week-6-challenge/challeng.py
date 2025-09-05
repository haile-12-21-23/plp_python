import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file

data=pd.read_csv('sales_data.csv')


# Analysis

# 1.Total revenue
total_revenue=data['Revenue ($)'].sum()

# 2 Best-selling product

best_selling=data.groupby('Product')['Quantity Sold'].sum().idxmax()
best_selling_quantity=data.groupby('Product')['Quantity Sold'].sum().max()

# #Highest sales day

highest_selling_day=data.groupby('Date')['Revenue ($)'].sum().idxmax()
highest_selling_day_revenue=data.groupby('Date')['Revenue ($)'].sum().max()


# Save the results

summary=(
    f"Total Revenue: ${total_revenue:}\n"
    f"Best-selling Product:{best_selling} ({best_selling_quantity})\n"
    f"Highest Sale Day:{highest_selling_day} (${highest_selling_day_revenue})"
)

with open('sales_summary.txt','w') as f:
    f.write(summary)

# Print the insight in user-friendly format

print("Sales Analysis Results")

print("------------------------")
print(summary)


# Bonous: Visualization
plt.figure(figsize=(8,5))
daily_sales=data.groupby('Date')['Revenue ($)'].sum()
daily_sales.plot(kind='line', marker='o')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('daily_sales_trend.png')
plt.show()