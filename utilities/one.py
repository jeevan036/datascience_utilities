import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

class DataPreprocessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.load_data()

    def load_data(self):
        """Load data from CSV file."""
        try:
            self.data = pd.read_csv(self.file_path)
            print(f"Data loaded successfully from {self.file_path}")
        except Exception as e:
            print(f"Error loading data: {e}")
            self.data = None

    def handle_missing_values(self):
        """Handle missing values by filling them or dropping."""
        if self.data is not None:
            print("\nHandling Missing Values:")
            # Fill numerical missing values with the mean and categorical with the mode
            num_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
            cat_cols = self.data.select_dtypes(include=['object']).columns

            # Using SimpleImputer for numerical and categorical columns
            imputer = ColumnTransformer(
                transformers=[
                    ('num', SimpleImputer(strategy='mean'), num_cols),
                    ('cat', SimpleImputer(strategy='most_frequent'), cat_cols)
                ]
            )
            
            # Apply imputation to the data
            self.data[num_cols] = imputer.transform(self.data[num_cols])
            self.data[cat_cols] = imputer.transform(self.data[cat_cols])

            print("Missing values handled successfully.")
        else:
            print("No data to process.")

    def encode_categorical_variables(self):
        """Encode categorical variables using one-hot encoding."""
        if self.data is not None:
            print("\nEncoding Categorical Variables:")
            cat_cols = self.data.select_dtypes(include=['object']).columns

            # One-Hot Encoding using pandas get_dummies
            self.data = pd.get_dummies(self.data, columns=cat_cols, drop_first=True)
            print("Categorical variables encoded successfully.")
        else:
            print("No data to process.")

    def scale_numerical_features(self, method='standard'):
        """Scale numerical features."""
        if self.data is not None:
            print(f"\nScaling Numerical Features using {method.capitalize()} Scaling:")
            num_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
            
            # Choose scaling method
            if method == 'standard':
                scaler = StandardScaler()
            elif method == 'minmax':
                scaler = MinMaxScaler()
            else:
                print("Invalid scaling method. Using Standard Scaling by default.")
                scaler = StandardScaler()

            # Apply scaling
            self.data[num_cols] = scaler.fit_transform(self.data[num_cols])
            print(f"Numerical features scaled using {method.capitalize()} scaling.")
        else:
            print("No data to process.")

    def split_data(self, target_column, test_size=0.2):
        """Split data into training and testing sets."""
        if self.data is not None:
            print(f"\nSplitting Data into Training and Testing sets:")
            X = self.data.drop(columns=[target_column])
            y = self.data[target_column]
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
            print("Data split into training and testing sets successfully.")
            return X_train, X_test, y_train, y_test
        else:
            print("No data to split.")
            return None, None, None, None

    def preprocess(self, target_column, scaling_method='standard', test_size=0.2):
        """Full data preprocessing pipeline."""
        self.handle_missing_values()
        self.encode_categorical_variables()
        self.scale_numerical_features(scaling_method)
        return self.split_data(target_column, test_size)

def main():
    file_path = input("Enter the path to the CSV file: ")
    target_column = input("Enter the target column name: ")
    scaling_method = input("Enter scaling method ('standard' or 'minmax'): ").lower()
    test_size = float(input("Enter the test size ratio (e.g., 0.2 for 20%): "))

    preprocessor = DataPreprocessor(file_path)
    X_train, X_test, y_train, y_test = preprocessor.preprocess(target_column, scaling_method, test_size)

    if X_train is not None:
        print(f"\nTraining set shape: {X_train.shape}")
        print(f"Test set shape: {X_test.shape}")
    else:
        print("Data preprocessing failed.")

if __name__ == "__main__":
    main()

