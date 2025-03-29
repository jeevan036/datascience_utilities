import pandas as pd
import matplotlib.pyplot as plt

# Create a simple dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 35, 40, 22],
    'Salary': [50000, 60000, 75000, 90000, 45000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display basic statistics
print(df.describe())

# Plot Age vs Salary
plt.scatter(df['Age'], df['Salary'], color='blue', label='Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary Distribution')
plt.legend()
plt.show()
