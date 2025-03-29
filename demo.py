import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Create a simple dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 18, 45],
    'Score': [85, 92, 78, 88]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display basic statistics
print("Basic Statistics:")
print(df.describe())

# Visualize the data: Bar chart for scores
plt.bar(df['Name'], df['Score'], color='skyblue')
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Scores of Individuals')
plt.show()