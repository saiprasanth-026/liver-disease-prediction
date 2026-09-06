"""
train_model.py
---------------
This is the "data science" half of the project - the part you preprocess,
train, and evaluate. Kept intentionally simple so you can explain every line.

Steps (say these out loud in the interview):
1. Load the dataset (Pandas)
2. Encode the categorical 'Gender' column
3. Handle missing values
4. Split into train/test sets
5. Scale the numeric features
6. Train a RandomForestClassifier (Scikit-learn)
7. Evaluate accuracy
8. Save the trained model + scaler with joblib so the Flask app can reuse them
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# 1. Load data
df = pd.read_csv("dataset.csv")

# 2. Encode Gender: Male -> 1, Female -> 0
df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})

# 3. Handle any missing values (fill with column mean) - real ILPD data has a few
df.fillna(df.mean(numeric_only=True), inplace=True)

FEATURES = [
    "Age", "Gender", "Total_Bilirubin", "Direct_Bilirubin",
    "Alkaline_Phosphotase", "Alamine_Aminotransferase",
    "Aspartate_Aminotransferase", "Total_Proteins", "Albumin",
    "Albumin_and_Globulin_Ratio"
]
TARGET = "Diagnosis"

X = df[FEATURES]
y = df[TARGET]

# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Scale features (helps the model treat all features fairly)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Train model
model = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42)
model.fit(X_train_scaled, y_train)

# 7. Evaluate
y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print(f"Model accuracy on test set: {acc*100:.2f}%")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Feature importance - good talking point for interview
importances = pd.Series(model.feature_importances_, index=FEATURES).sort_values(ascending=False)
print("\nTop features driving the prediction:\n", importances.head(5))

# 8. Save model + scaler for the Flask app
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
print("\nSaved model.pkl and scaler.pkl")
