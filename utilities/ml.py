import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def ml_pipeline(csv_file, target_column):
    df = pd.read_csv(csv_file)
    df = df.dropna()  # Remove rows with missing values
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy on test set: {accuracy:.4f}")
    
    cross_val_scores = cross_val_score(model, X, y, cv=5)
    print(f"Cross-validation accuracy: {cross_val_scores.mean():.4f} (+/- {cross_val_scores.std():.4f})")

ml_pipeline('data.csv', 'target_column')
