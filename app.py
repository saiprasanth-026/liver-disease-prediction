"""
app.py
------
Flask web app for the Liver Disease Prediction System.

Flow:
1. User fills a form with liver function test values (home page)
2. Flask receives the POST request at /predict
3. We scale the inputs using the SAME scaler used during training
4. The saved RandomForest model predicts: 0 = healthy, 1 = liver disease
5. We show the result with a confidence score and top contributing features
"""

from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model + scaler once when the server starts
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

FEATURES = [
    "Age", "Gender", "Total_Bilirubin", "Direct_Bilirubin",
    "Alkaline_Phosphotase", "Alamine_Aminotransferase",
    "Aspartate_Aminotransferase", "Total_Proteins", "Albumin",
    "Albumin_and_Globulin_Ratio"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # 1. Collect form data
    form = request.form
    gender_value = 1 if form["Gender"] == "Male" else 0

    input_dict = {
        "Age": float(form["Age"]),
        "Gender": gender_value,
        "Total_Bilirubin": float(form["Total_Bilirubin"]),
        "Direct_Bilirubin": float(form["Direct_Bilirubin"]),
        "Alkaline_Phosphotase": float(form["Alkaline_Phosphotase"]),
        "Alamine_Aminotransferase": float(form["Alamine_Aminotransferase"]),
        "Aspartate_Aminotransferase": float(form["Aspartate_Aminotransferase"]),
        "Total_Proteins": float(form["Total_Proteins"]),
        "Albumin": float(form["Albumin"]),
        "Albumin_and_Globulin_Ratio": float(form["Albumin_and_Globulin_Ratio"]),
    }

    # 2. Build a DataFrame in the same column order used for training
    input_df = pd.DataFrame([input_dict])[FEATURES]

    # 3. Scale using the saved scaler
    input_scaled = scaler.transform(input_df)

    # 4. Predict class + probability
    prediction = int(model.predict(input_scaled)[0])
    probabilities = model.predict_proba(input_scaled)[0]
    confidence = round(max(probabilities) * 100, 1)

    # 5. Get top 3 features driving predictions overall (feature importance)
    importances = pd.Series(model.feature_importances_, index=FEATURES)
    top_features = importances.sort_values(ascending=False).head(3)
    top_features_list = [(name, round(val * 100, 1)) for name, val in top_features.items()]

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence,
        top_features=top_features_list
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
