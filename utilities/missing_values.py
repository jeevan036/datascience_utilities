import pandas as pd

def handle_missing_values(df: pd.DataFrame, strategy: str = 'mean', columns: list = None):
    """
    Handle missing values in a DataFrame.

    Parameters:
    df (pd.DataFrame): Input DataFrame
    strategy (str): Strategy to handle missing values ('mean', 'median', 'mode', 'drop')
    columns (list): List of columns to apply the strategy (default is all columns)

    Returns:
    pd.DataFrame: DataFrame with missing values handled
    """
    if columns is None:
        columns = df.columns
    
    if strategy == 'mean':
        df[columns] = df[columns].fillna(df[columns].mean())
    elif strategy == 'median':
        df[columns] = df[columns].fillna(df[columns].median())
    elif strategy == 'mode':
        for col in columns:
            df[col] = df[col].fillna(df[col].mode()[0])
    elif strategy == 'drop':
        df = df.dropna(subset=columns)
    else:
        raise ValueError("Invalid strategy. Choose from 'mean', 'median', 'mode', or 'drop'")
    
    return df

# Example Usage
if __name__ == "__main__":
    data = {'A': [1, 2, None, 4], 'B': [None, 2, 3, 4]}
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)
    df = handle_missing_values(df, strategy='mean')
    print("Processed DataFrame:\n", df)
