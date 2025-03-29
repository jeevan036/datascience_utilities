import pandas as pd
from sklearn.impute import SimpleImputer

def handle_missing_values(df, strategy="mean", columns=None):
    """
    Handles missing values in a dataframe by either filling or removing them.

    Parameters:
    df (pd.DataFrame): The input dataframe with missing values.
    strategy (str): The strategy for filling missing values. Options: 'mean', 'median', 'most_frequent', 'constant'. Default is 'mean'.
    columns (list): List of columns to apply the imputation. If None, it will apply to all columns with missing values.

    Returns:
    pd.DataFrame: The dataframe with missing values handled.
    """
    imputer = SimpleImputer(strategy=strategy)

    # Apply imputation only to specified columns or all columns with missing values
    if columns:
        df[columns] = imputer.fit_transform(df[columns])
    else:
        df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

    return df

def remove_missing_values(df, columns=None):
    """
    Removes rows with missing values from the dataframe.

    Parameters:
    df (pd.DataFrame): The input dataframe with missing values.
    columns (list): List of columns to remove missing values. If None, removes rows with any missing values.

    Returns:
    pd.DataFrame: The dataframe with rows containing missing values removed.
    """
    if columns:
        df = df.dropna(subset=columns)
    else:
        df = df.dropna()

    return df

if _name_ == "_main_":
    # Example usage
    data = {'A': [1, 2, None, 4],
            'B': [None, 2, 3, 4],
            'C': [1, None, 3, 4]}

    df = pd.DataFrame(data)

    # Fill missing values with mean
    df_filled = handle_missing_values(df, strategy='mean')
    print("Filled Missing Values:\n", df_filled)

    # Remove rows with missing values
    df_dropped = remove_missing_values(df)
    print("\nDropped Missing Values:\n", df_dropped) 