import numpy as np
import pandas as pd

def min_max_normalize(df, columns=None):
    """
    Applies Min-Max Normalization to the specified columns in a DataFrame.

    Parameters:
        df (pd.DataFrame): Input DataFrame
        columns (list, optional): List of column names to normalize. If None, all numeric columns are normalized.

    Returns:
        pd.DataFrame: DataFrame with normalized values
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns

    df_normalized = df.copy()
    for col in columns:
        min_val = df[col].min()
        max_val = df[col].max()
        df_normalized[col] = (df[col] - min_val) / (max_val - min_val)

    return df_normalized

# Example usage
if __name__ == "__main__":
    data = {"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)
    print(min_max_normalize(df))
