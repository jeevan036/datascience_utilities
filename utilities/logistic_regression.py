import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def logistic_regression(X, y, test_size=0.2, random_state=42):
    """
    Train a Logistic Regression model on the provided dataset.
    
    Parameters:
    - X: Features (numpy array or pandas DataFrame)
    - y: Target labels (numpy array or pandas Series)
    - test_size: Proportion of data to use for testing (default: 0.2)
    - random_state: Random seed for reproducibility (default: 42)
    
    Returns:
    - model: Trained Logistic Regression model
    - accuracy: Accuracy of the model on the test set
    - conf_matrix: Confusion matrix
    - class_report: Classification report
    """
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Initialize the Logistic Regression model
    model = LogisticRegression(max_iter=1000)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Generate confusion matrix and classification report
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)
    
    # Return the trained model and performance metrics
    return model, accuracy, conf_matrix, class_report

# Example usage:
# X and y should be your features and target labels
# model, accuracy, conf_matrix, class_report = logistic_regression(X, y)
# print(f'Accuracy: {accuracy}')
# print(f'Confusion Matrix:\n{conf_matrix}')
# print(f'Classification Report:\n{class_report}')

