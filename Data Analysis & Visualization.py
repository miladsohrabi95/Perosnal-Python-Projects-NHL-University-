import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
data = {
    'id': np.arange(1, 11),
    'name': ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia', 'James', 'Amelia', 'Benjamin', 'Isabella'],
    'age': np.random.randint(20, 40, size=10),
    'gender': np.random.choice(['Male', 'Female'], size=10),
    'sales': np.random.randint(1000, 5000, size=10),
    'region': np.random.choice(['East', 'West', 'North', 'South'], size=10)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to a CSV file
df.to_csv('sample_dataset.csv', index=False)

# Read the dataset
df = pd.read_csv('sample_dataset.csv')

# Perform data analysis
# For example, calculate the Average sales by each region!
average_sales_by_region = df.groupby('region')['sales'].mean()


# Visualizing the data
average_sales_by_region.plot(kind='bar', color='skyblue')
plt.title('Average Sales by Region')
plt.xlabel('Region')
plt.ylabel('Average Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

