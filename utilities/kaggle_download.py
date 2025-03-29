import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_dataset(dataset, save_path="datasets/"):
    """Downloads a dataset from Kaggle and saves it to the specified path."""
    api = KaggleApi()
    api.authenticate()

    os.makedirs(save_path, exist_ok=True)
    api.dataset_download_files(dataset, path=save_path, unzip=True)
    print(f"Dataset '{dataset}' downloaded successfully to {save_path}")

# Example usage
if __name__ == "__main__":
    dataset_name = "zynicide/wine-reviews"  # Change this to any Kaggle dataset
    download_kaggle_dataset(dataset_name)
