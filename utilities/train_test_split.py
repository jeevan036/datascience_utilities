import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Splits the dataset into training and testing sets.

    Parameters:
        X (pandas.DataFrame or numpy.ndarray): Feature matrix.
        y (pandas.Series or numpy.ndarray): Target labels.
        test_size (float): Proportion of the dataset to include in the test split (default=0.2).
        random_state (int): Random seed for reproducibility (default=42).

    Returns:
        X_train, X_test, y_train, y_test (tuple): Splitted dataset.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# Example usage
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'feature1': range(1, 101),
        'feature2': range(101, 201),
        'label': [0 if i < 50 else 1 for i in range(100)]
    })

    X = data[['feature1', 'feature2']]
    y = data['label']

    X_train, X_test, y_train, y_test = split_data(X, y)
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Testing set size: {X_test.shape[0]}")
