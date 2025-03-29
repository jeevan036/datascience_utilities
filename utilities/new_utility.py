import numpy as np

def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

if __name__ == "__main__":
    sample_data = np.array([10, 20, 30, 40, 50])
    print(normalize_data(sample_data))
