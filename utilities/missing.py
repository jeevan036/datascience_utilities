import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, np.nan, np.nan, 4, 5],
    'D': [np.nan, np.nan, np.nan, 4, 5]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")

# Detect missing values
print("Missing Values Detection:")
print(df.isnull())
print("\n")

# Count missing values per column
print("Count of Missing Values Per Column:")
print(df.isnull().sum())
print("\n")

# Drop rows with any missing values
df_dropped_rows = df.dropna()
print("DataFrame after dropping rows with missing values:")
print(df_dropped_rows)
print("\n")

# Drop columns with any missing values
df_dropped_cols = df.dropna(axis=1)
print("DataFrame after dropping columns with missing values:")
print(df_dropped_cols)
print("\n")

# Fill missing values with a specific value
df_filled = df.fillna(0)
print("DataFrame after filling missing values with 0:")
print(df_filled)
print("\n")

# Fill missing values with column mean
df_filled_mean = df.fillna(df.mean())
print("DataFrame after filling missing values with column mean:")
print(df_filled_mean)
print("\n")

# Fill missing values forward (previous value)
df_filled_ffill = df.fillna(method='ffill')
print("DataFrame after forward fill (ffill):")
print(df_filled_ffill)
print("\n")

# Fill missing values backward (next value)
df_filled_bfill = df.fillna(method='bfill')
print("DataFrame after backward fill (bfill):")
print(df_filled_bfill)
print("\n")

# Interpolate missing values
df_interpolated = df.interpolate(method='linear')
print("DataFrame after linear interpolation:")
print(df_interpolated)
