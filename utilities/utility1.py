import os
import numpy as np
from sklearn.linear_model import LinearRegression

def generate_random_data(size=10):
    """
    Generates random data for simple linear regression.
    """
    X = np.random.rand(size, 1) * 10  # Features
    y = 2 * X + np.random.randn(size, 1) * 2  # Labels with noise
    return X, y

def train_linear_regression(X, y):
    """
    Trains a simple linear regression model.
    """
    model = LinearRegression()
    model.fit(X, y)
    return model

def main():
    X, y = generate_random_data()
    model = train_linear_regression(X, y)
    print("Model Coefficients:", model.coef_)
    print("Model Intercept:", model.intercept_)

if __name__ == "__main__":
    main()
