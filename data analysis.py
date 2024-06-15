import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gaussian_kde


df = pd.read_csv('C:/Users/akhi2/Downloads/sales_data.csv')  # Adjust

# Display the first few rows of the dataframe
print("First few rows of the dataset:")
print(df.head())

# Data exploration tasks

# Filtering data for a specific store
store_a_data = df[df['Day'] == 'Store A']
print("\nData for Store A:")
print(store_a_data)

# Sorting data by date and quantity
sorted_data = df.sort_values(by=['Date', 'Order_Quantity'], ascending=[True, False])
print("\nData sorted by date and quantity:")
print(sorted_data)

# Grouping data by store and product, and calculating the total quantity sold
grouped_data =df.groupby(['Day', 'Product'])['Order_Quantity'].sum().reset_index()
print("\nTotal quantity sold by store and product:")
print(grouped_data)

# Summary statistics
print("\nSummary statistics for quantity:")
print("Mean:", df['Order_Quantity'].mean())
print("Median:", df['Order_Quantity'].median())
print("Standard Deviation:", df['Order_Quantity'].std())

# Data visualization

# Bar plot of total quantity sold by store and product
plt.figure(figsize=(10, 6))
sns.barplot(x='Day', y='Order_Quantity', hue='Product', data=grouped_data)
plt.title('Total Quantity Sold by Store and Product')
plt.show()

# Distribution of quantities sold
plt.figure(figsize=(10, 6))
sns.histplot(df['Order_Quantity'], kde=True)
plt.title('Distribution of Quantities Sold')
plt.xlabel('Order_Quantity')
plt.ylabel('Frequency')
plt.show()

# Box plot of price distributions by store
plt.figure(figsize=(10, 6))
sns.boxplot(x='Day', y='Unit_Price', data=df)
plt.title('Price Distribution by Store')
plt.show()
