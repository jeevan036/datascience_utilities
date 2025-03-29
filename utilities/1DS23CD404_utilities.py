print("Hello students, Add utilities to this folder")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Sample dataset with missing values
data = {
    'A': [1, 2, np.nan, 4, 5, np.nan, 7],
    'B': [np.nan, 2, 3, np.nan, 5, 6, 7],
    'C': [1, np.nan, 3, 4, 5, 6, np.nan]
}
df = pd.DataFrame(data)

# Display the dataset
print("Original Dataset:")
print(df)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Visualizing missing values
sns.heatmap(df.isnull(), cmap='viridis', cbar=False, yticklabels=False)
plt.title("Missing Values Heatmap")
plt.show()

# Handling missing values
# Option 1: Drop rows with missing values
df_dropna = df.dropna()
print("\nDataset after dropping missing values:")
print(df_dropna)

# Option 2: Fill missing values with a specific value (e.g., mean of column)
df_fillna = df.fillna(df.mean())
print("\nDataset after filling missing values with mean:")
print(df_fillna)

# Option 3: Forward fill
df_ffill = df.ffill()
print("\nDataset after forward fill:")
print(df_ffill)

# Option 4: Backward fill
df_bfill = df.bfill()
print("\nDataset after backward fill:")
print(df_bfill)

# Normalization using Min-Max Scaling
scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df_fillna), columns=df_fillna.columns)
print("\nDataset after Min-Max Normalization:")
print(df_normalized)

# Standardization using StandardScaler
scaler_standard = StandardScaler()
df_standardized = pd.DataFrame(scaler_standard.fit_transform(df_fillna), columns=df_fillna.columns)
print("\nDataset after Standardization:")
print(df_standardized)
