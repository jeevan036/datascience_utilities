import pandas as pd
from io import StringIO

def report_missing_values(df):
    """
    Print the number of missing values per column in the given DataFrame.
    """
    missing = df.isnull().sum()
    print("Missing values per column:")
    print(missing)

if __name__ == "__main__":
    # Sample CSV data embedded in the code.
    csv_data = """
Name,Age,Salary
John,28,50000
Alice,,60000
Bob,35,
,42,70000
"""
    # Read the CSV data from the string using StringIO
    df = pd.read_csv(StringIO(csv_data.strip()))
    
    # Display the DataFrame
    print("Sample Data:")
    print(df)
    print("\n")
    
    # Report missing values
    report_missing_values(df)
