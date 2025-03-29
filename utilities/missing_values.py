# missing_values.py

import pandas as pd

def fill_missing_values(df, method='mean', column=None, value=None):
    """
    Fills missing values in a DataFrame.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
        method (str): The method to fill missing values. Can be 'mean', 'median', or 'mode'.
        column (str): The specific column to fill missing values in (if None, fills all columns).
        value (any): A specific value to replace missing values with (if specified).
    
    Returns:
        pd.DataFrame: The DataFrame with missing values filled.
    """
    if value is not None:
        # Replace missing values with the provided value
        if column:
            df[column] = df[column].fillna(value)
        else:
            df = df.fillna(value)
    elif method == 'mean':
        # Fill missing values with the mean of the column
        if column:
            df[column] = df[column].fillna(df[column].mean())
        else:
            df = df.fillna(df.mean())
    elif method == 'median':
        # Fill missing values with the median of the column
        if column:
            df[column] = df[column].fillna(df[column].median())
        else:
            df = df.fillna(df.median())
    elif method == 'mode':
        # Fill missing values with the mode of the column
        if column:
            df[column] = df[column].fillna(df[column].mode()[0])
        else:
            df = df.fillna(df.mode().iloc[0])
    
    return df

def remove_missing_values(df, axis=0):
    """
    Removes rows or columns with missing values.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
        axis (int): Axis to drop missing values along. 0 for rows, 1 for columns.
    
    Returns:
        pd.DataFrame: The DataFrame with rows/columns containing missing values removed.
    """
    return df.dropna(axis=axis)

def main():
    # Sample DataFrame with missing values
    data = {
        'A': [1, 2, None, 4, 5],
        'B': [None, 2, 3, 4, 5],
        'C': [1, None, 3, None, 5],
    }
    
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)

    # Fill missing values with the mean of the column
    filled_df = fill_missing_values(df, method='mean')
    print("\nDataFrame with missing values filled (mean):")
    print(filled_df)

    # Remove rows with missing values
    removed_df = remove_missing_values(df, axis=0)
    print("\nDataFrame with rows containing missing values removed:")
    print(removed_df)

    # Fill missing values with a specific value
    filled_specific_df = fill_missing_values(df, value=0)
    print("\nDataFrame with missing values filled with 0:")
    print(filled_specific_df)

if __name__ == "__main__":
    main()
