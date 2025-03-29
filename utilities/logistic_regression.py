import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_logistic_regression(X, y):
    """
    Trains a logistic regression model and returns accuracy.
    
    Parameters:
        X (numpy.ndarray or pandas.DataFrame): Feature matrix.
        y (numpy.ndarray or pandas.Series): Target labels.
    
    Returns:
        model (LogisticRegression): Trained logistic regression model.
        accuracy (float): Accuracy score on the test set.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return model, accuracy

# Example usage:
if __name__ == "__main__":
    # Sample data
    X = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8]])
    y = np.array([0, 0, 0, 1, 1, 1])

    model, acc = train_logistic_regression(X, y)
    print(f"Model trained with accuracy: {acc:.2f}")
