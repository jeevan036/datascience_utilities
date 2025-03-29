import pandas as pd

# Example dataset
data = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, 3, 2, 1]
})

# Filling missing values
filled_data = fill_missing_values(data)
print(filled_data)

# Standardizing data
standardized_data = standardize_data(data)
print(standardized_data)
