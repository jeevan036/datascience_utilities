import pandas as pd

# Sample data
data = {
    "A": [1, 2, None, 4],
    "B": [None, 2, 3, None],
    "C": [10, None, 30, 40]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Fill missing values with column mean
df_filled = df.fillna(df.mean(numeric_only=True))
print("\nDataFrame after filling missing values:\n", df_filled)

# Remove rows with missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:\n", df_dropped)
