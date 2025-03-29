import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib

def train_and_save_model(X, y, model_path="model.pkl"):
    # Normalize features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    # Train model
    model = LinearRegression()
    model.fit(X, y)
    
    # Save model and scaler
    joblib.dump((model, scaler), model_path)
    print(f"Model saved to {model_path}")

def load_model_and_predict(model_path, new_data):
    # Load model
    model, scaler = joblib.load(model_path)
    
    # Transform new data
    new_data = scaler.transform([new_data])
    
    # Predict
    prediction = model.predict(new_data)
    return prediction[0]

if __name__ == "__main__":
    # Example usage
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([2, 3, 4, 5])
    
    train_and_save_model(X, y)
    print(load_model_and_predict("model.pkl", [2, 3]))
