import pandas as pd

def detect_missing_values(df):
    """
    Detect missing values in a DataFrame.
    Args:
    df (pd.DataFrame): Input DataFrame.
    Returns:
    pd.DataFrame: DataFrame showing count and percentage of missing values per column.
    """
    missing_count = df.isnull().sum()
    missing_percentage = (missing_count / len(df)) * 100
    return pd.DataFrame({'Missing Count': missing_count, 'Missing Percentage': missing_percentage})

def fill_missing_values(df, method='mean', columns=None):
    """
    Fill missing values using specified method.
    Args:
    df (pd.DataFrame): Input DataFrame.
    method (str): Method to fill missing values - 'mean', 'median', 'mode', or 'ffill', 'bfill'.
    columns (list): Specific columns to fill. If None, all columns will be considered.
    Returns:
    pd.DataFrame: DataFrame with missing values filled.
    """
    if columns is None:
        columns = df.columns

    if method == 'mean':
        df[columns] = df[columns].fillna(df[columns].mean())
    elif method == 'median':
        df[columns] = df[columns].fillna(df[columns].median())
    elif method == 'mode':
        for col in columns:
            df[col].fillna(df[col].mode()[0], inplace=True)
    elif method in ['ffill', 'bfill']:
        df[columns] = df[columns].fillna(method=method)
    else:
        raise ValueError("Unsupported fill method. Choose from 'mean', 'median', 'mode', 'ffill', or 'bfill'.")

    return df

def drop_missing_values(df, threshold=0.5):
    """
    Drop columns with missing values exceeding a threshold.
    Args:
    df (pd.DataFrame): Input DataFrame.
    threshold (float): Fraction of missing values allowed (0 to 1).
    Returns:
    pd.DataFrame: DataFrame with columns removed if missing percentage exceeds threshold.
    """
    missing_percentage = df.isnull().mean()
    columns_to_drop = missing_percentage[missing_percentage > threshold].index
    return df.drop(columns=columns_to_drop)

if __name__ == '__main__':
    print("Utility for handling missing values. Import this module and use the functions as needed.")
