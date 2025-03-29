import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 120000, 95000, 68000]
}

df = pd.DataFrame(data)

# Utility Function 1: Load Dataset
def load_data(file_path, file_type='csv'):
    """
    Load a dataset from a given file path.
    Args:
        file_path (str): The file path to the dataset.
        file_type (str): The file type, default is 'csv'. Can be 'csv', 'excel', etc.
    Returns:
        pandas.DataFrame: Loaded data as a DataFrame.
    """
    if file_type == 'csv':
        return pd.read_csv(file_path)
    elif file_type == 'excel':
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

# Utility Function 2: Data Cleaning
def clean_data(df):
    """
    Clean the DataFrame by handling missing values, duplicates, and ensuring correct data types.
    Args:
        df (pandas.DataFrame): The dataframe to clean.
    Returns:
        pandas.DataFrame: Cleaned dataframe.
    """
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Handle missing values (fill with mean for numeric columns, mode for categorical)
    for col in df.columns:
        if df[col].dtype == np.number:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
    
    return df

# Utility Function 3: Exploratory Data Analysis (EDA)
def basic_eda(df):
    """
    Perform basic exploratory data analysis (EDA) on the dataset.
    Args:
        df (pandas.DataFrame): The dataframe to analyze.
    Returns:
        None
    """
    print("Basic EDA Overview")
    print("-------------------")
    print(f"Shape of the dataset: {df.shape}")
    print(f"Columns in the dataset: {df.columns.tolist()}")
    print(f"Missing values: \n{df.isnull().sum()}")
    print(f"Basic statistics (for numerical columns): \n{df.describe()}")
    
    # Visualize missing data
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title("Missing Data Visualization")
    plt.show()

# Utility Function 4: Data Visualization
def plot_distribution(df, column):
    """
    Plot the distribution of a specific column (numeric).
    Args:
        df (pandas.DataFrame): The dataframe containing the column.
        column (str): The column name to plot.
    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()


# Utility Function 5: Feature Scaling (Standardization)
def scale_data(df):
    """
    Scale the numeric columns of the DataFrame using standardization (z-score).
    Args:
        df (pandas.DataFrame): The dataframe to scale.
    Returns:
        pandas.DataFrame: DataFrame with scaled features.
    """
    from sklearn.preprocessing import StandardScaler
    
    scaler = StandardScaler()
    df_scaled = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    df_scaled[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df_scaled

# Utility Function 6: Train-Test Split
def split_data(df, target_column, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.
    Args:
        df (pandas.DataFrame): The dataframe to split.
        target_column (str): The name of the target column.
        test_size (float): Proportion of the dataset to include in the test split (default 0.2).
        random_state (int): Random seed for reproducibility.
    Returns:
        X_train, X_test, y_train, y_test: The split data.
    """
    from sklearn.model_selection import train_test_split
    
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    return X_train, X_test, y_train, y_test

# Example usage:
if __name__ == "__main__":
    # Clean the sample DataFrame
    df_cleaned = clean_data(df)
    
    # Perform basic EDA
    basic_eda(df_cleaned)
    
    # Plot distribution for 'Age' column
    plot_distribution(df_cleaned, 'Age')
    
    # Scale data
    df_scaled = scale_data(df_cleaned)
    
    # Split data into train and test sets (using 'Salary' as target column)
    X_train, X_test, y_train, y_test = split_data(df_scaled, 'Salary')

    # Print output of splits for verification
    print("Training Set (X_train, y_train):")
    print(X_train.head(), y_train.head())
    print("\nTest Set (X_test, y_test):")
    print(X_test.head(), y_test.head())

