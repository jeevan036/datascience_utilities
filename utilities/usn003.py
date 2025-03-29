import pandas as pd

# Creating a simple DataFrame
data = {
    'Color': ['Red', 'Blue', 'Green', 'Red', 'Green'],
    'Size': ['S', 'M', 'L', 'M', 'S']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Performing one-hot encoding
encoded_df = pd.get_dummies(df, columns=['Color', 'Size'])

print("\nOne-Hot Encoded DataFrame:")
print(encoded_df)