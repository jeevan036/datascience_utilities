import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = {'Category': ['A', 'B', 'C', 'D', 'E'],
        'Values': [23, 45, 56, 78, 33]}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(8, 5))
sns.barplot(x='Category', y='Values', data=df, palette='viridis')

# Adding labels and title
plt.title('Sample Bar Chart')
plt.xlabel('Category')
plt.ylabel('Values')


plt.show()
