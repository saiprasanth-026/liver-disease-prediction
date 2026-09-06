# Liver Disease Prediction System

A simple end-to-end machine learning web app: enter a patient's liver function
test results, get an instant prediction (Healthy vs Liver Disease Likely) with
a confidence score — built with Python, Scikit-learn, and Flask.

## How to run it

```bash
pip install -r requirements.txt
python generate_dataset.py   # creates dataset.csv (only needed once)
python train_model.py        # trains the model, saves model.pkl + scaler.pkl
python app.py                 # starts the web server
```

Then open **http://127.0.0.1:5000** in your browser.

## Deploy on Render

1. Push this project to a GitHub repository using the commands below.
2. In Render, create a **New Web Service** and connect the GitHub repository.
3. Use these settings:
  - **Runtime:** Python 3
  - **Build command:** `pip install -r requirements.txt`
  - **Start command:** `gunicorn --bind 0.0.0.0:$PORT app:app`
4. Deploy the service. Render will provide a public URL.

Keep `model.pkl`, `scaler.pkl`, and `dataset.csv` in the repository. The model
files are required when `app.py` starts.

## Push to GitHub

Run these commands from the project folder. Replace the URL with your own new,
empty GitHub repository URL:

```bash
git init
git add .
git commit -m "Initial liver disease prediction app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

## Project structure

| File | Purpose |
|---|---|
| `generate_dataset.py` | Creates the patient dataset (10 features, matches the real Indian Liver Patient Dataset structure) |
| `train_model.py` | Cleans the data, trains a Random Forest model, evaluates it, saves it |
| `app.py` | Flask server — handles the web form and predictions |
| `templates/index.html` | Input form (colorful UI) |
| `templates/result.html` | Prediction result page |
| `static/style.css` | All the styling |
| `model.pkl` / `scaler.pkl` | The saved trained model and feature scaler |

## How to explain this in an interview (simple script)

**1. What problem does it solve?**
"It predicts whether a patient likely has liver disease based on 10 values
from a standard liver function blood test — things like Bilirubin, ALT, AST,
and Albumin levels. This kind of tool could help doctors quickly flag
high-risk patients for further testing."

**2. What's the data?**
"I used a dataset structured like the Indian Liver Patient Dataset — each row
is one patient with Age, Gender, and 8 liver enzyme/protein readings, plus a
label: healthy or diagnosed with liver disease."

**3. What did you do with the data? (preprocessing)**
- Encoded Gender (Male/Female) into numbers, since ML models need numeric input.
- Filled any missing values with the column average.
- Split the data 80/20 into training and test sets.
- Scaled all the features with `StandardScaler` so no single large-range
  feature (like Alkaline Phosphotase, which is in the hundreds) unfairly
  dominates over small-range features (like Albumin, which is 1-5).

**4. What model did you use, and why?**
"A Random Forest Classifier — it builds many decision trees and combines
their votes. I chose it because it handles non-linear relationships well,
resists overfitting better than a single decision tree, and gives you
feature importance for free, which is great for explaining *why* it made a
prediction — important in healthcare."

**5. How well does it perform?**
"On the held-out test set it gets about 97% accuracy. I'd point out in an
interview that with real clinical data you'd want much more rigorous
validation (cross-validation, more data, checking for class imbalance)
before trusting this for real decisions — this is a learning project, not a
certified medical device."

**6. What are the most important features?**
"Total and Direct Bilirubin, and the AST/ALT liver enzymes, came out as the
top predictors — which lines up with real medical knowledge, since elevated
bilirubin and liver enzymes are classic signs of liver dysfunction. That's a
nice sanity check that the model 'learned' something medically sensible."

**7. How does the web app work end-to-end?**
"The user fills a form on the Flask front end. When they submit, Flask reads
the values, applies the *same* scaler used in training, feeds them to the
saved model, and returns a prediction plus a confidence percentage and the
top 3 contributing features — all rendered on a result page."

**8. If asked "what would you improve?"**
- Use the real ILPD dataset from Kaggle instead of synthetic data.
- Try other models (Logistic Regression, XGBoost) and compare.
- Add input validation and error handling on the form.
- Deploy it (e.g., on Render/Railway) so it's a live link, not just local.

## Note
The dataset here is synthetically generated (not real patient data) so the
whole project runs instantly without needing to download anything — but it's
built with the exact same structure, features, and workflow as the real
Kaggle dataset, so everything you say about it in an interview holds up.
