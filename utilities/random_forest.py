import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_random_forest(X, y, n_estimators=100, max_depth=None):
    """
    Trains a Random Forest classifier and returns accuracy.
    
    Parameters:
        X (numpy.ndarray or pandas.DataFrame): Feature matrix.
        y (numpy.ndarray or pandas.Series): Target labels.
        n_estimators (int): Number of trees in the forest (default=100).
        max_depth (int or None): Maximum depth of trees (default=None).
    
    Returns:
        model (RandomForestClassifier): Trained Random Forest model.
        accuracy (float): Accuracy score on the test set.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return model, accuracy

# Example usage:
if __name__ == "__main__":
    # Sample data
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)

    model, acc = train_random_forest(X, y)
    print(f"Model trained with accuracy: {acc:.2f}")
