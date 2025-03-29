import pandas as pd
from sklearn.model_selection import train_test_split

# URL of the dataset (replace with your actual dataset URL)
dataset_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"

# Load the dataset from the URL
data = pd.read_csv(dataset_url)

# Preview the data
print("First few rows of the dataset:")
print(data.head())

# Assuming the last column is the target variable and the rest are features
X = data.iloc[:, :-1].values  # All columns except the last one
y = data.iloc[:, -1].values   # Last column as target

# Split the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the resulting splits
print("\nTraining Features (X_train):")
print(X_train[:5])
print("\nTesting Features (X_test):")
print(X_test[:5])
print("\nTraining Labels (y_train):")
print(y_train[:5])
print("\nTesting Labels (y_test):")
print(y_test[:5])
