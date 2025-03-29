import pandas as pd
import json

def csv_to_json(csv_file, json_file):
    """Converts a CSV file to a JSON file."""
    df = pd.read_csv(csv_file)
    df.to_json(json_file, orient="records", indent=4)
    print(f"CSV data successfully converted to JSON and saved as {json_file}")

# Example usage
if __name__ == "__main__":
    csv_to_json("data.csv", "data.json")
