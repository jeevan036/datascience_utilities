import numpy as np
import pandas as pd

def standardize(data):
    """
    Standardizes the numerical columns in a dataset using Z-score normalization.
    
    Parameters:
        data (pd.DataFrame): Input dataframe containing numerical columns.
        
    Returns:
        pd.DataFrame: Standardized dataframe.
    """
    return (data - data.mean()) / data.std()

# Example usage:
if __name__ == "__main__":
    sample_data = pd.DataFrame({"values": [10, 20, 30, 40, 50]})
    standardized_data = standardize(sample_data)
    print(standardized_data)
