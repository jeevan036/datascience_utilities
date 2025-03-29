import tensorflow as tf
from tensorflow.keras import layers, models

def build_lstm(input_shape=(100, 1), num_classes=1):
    """
    Builds a simple LSTM model for time series forecasting.

    Parameters:
        input_shape (tuple): Shape of the input sequence (default=(100, 1)).
        num_classes (int): Number of output classes (default=1 for regression).

    Returns:
        model (tf.keras.Model): Compiled LSTM model.
    """
    model = models.Sequential([
        layers.LSTM(50, activation='relu', return_sequences=True, input_shape=input_shape),
        layers.LSTM(50, activation='relu'),
        layers.Dense(25, activation='relu'),
        layers.Dense(num_classes)  # Output layer (no activation for regression)
    ])

    model.compile(optimizer='adam',
                  loss='mse',  # Mean Squared Error for regression tasks
                  metrics=['mae'])  # Mean Absolute Error
    
    return model

# Example usage
if __name__ == "__main__":
    model = build_lstm()
    model.summary()
