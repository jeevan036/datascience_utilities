import numpy as np

def min_max_normalize(data):
    """Normalize the data using Min-Max Scaling"""
    return (data - np.min(data)) / (np.max(data) - np.min(data))

# Example usage
if __name__ == "__main__":
    sample_data = np.array([10, 20, 30, 40, 50])
    print(min_max_normalize(sample_data))
