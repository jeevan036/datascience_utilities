import os
import shutil
from datetime import datetime
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# ---------------------------
# 1. Train logistic model
# ---------------------------
def train_model():
    data = {
        "Age": [22, 25, 47, 52, 46, 56, 55, 60],
        "Salary": [25000, 27000, 42000, 50000, 52000, 60000, 58000, 62000],
        "Purchased": [0, 0, 1, 1, 1, 1, 1, 1]
    }

    df = pd.DataFrame(data)
    X = df[["Age", "Salary"]]
    y = df["Purchased"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"✅ Model trained with test accuracy: {accuracy:.2f}")

    # Save the model
    os.makedirs("models", exist_ok=True)
    model_path = "models/logistic_model.pkl"
    joblib.dump(model, model_path)
    print(f"📦 Model saved at: {model_path}")
    return model_path

# ---------------------------
# 2. Create a local version backup
# ---------------------------
def backup_files(model_path, script_path):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    version_dir = f"backups/version_{timestamp}"
    os.makedirs(version_dir, exist_ok=True)

    # Copy model
    shutil.copy(model_path, os.path.join(version_dir, "logistic_model.pkl"))
    
    # Copy this script
    shutil.copy(script_path, os.path.join(version_dir, os.path.basename(script_path)))

    print(f"🗂️ Backup saved to: {version_dir}")

# ---------------------------
# 3. Run everything
# ---------------------------
if __name__ == "__main__":
    model_path = train_model()
    backup_files(model_path, script_path=__file__)
