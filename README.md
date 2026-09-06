# Liver Disease Prediction System

An end-to-end machine learning web application that predicts whether a patient is **likely to have liver disease** based on liver function test results.

The application uses **Python, Scikit-learn, and Flask** to provide a simple interface where users can enter patient parameters and receive a prediction with a confidence score.

> **Disclaimer:** This is an educational machine learning project. It is not a medical diagnostic tool and should not be used for clinical decision-making.

---

## Features

* Predicts **Healthy** or **Liver Disease Likely**
* Accepts 10 patient-related features
* Handles data preprocessing automatically
* Uses a **Random Forest Classifier**
* Uses `StandardScaler` for feature scaling
* Displays prediction confidence
* Displays the top contributing features
* Simple Flask-based web interface
* Can be deployed as a public web application

---

## Technologies Used

| Technology   | Purpose                            |
| ------------ | ---------------------------------- |
| Python       | Core programming language          |
| Flask        | Web application framework          |
| Scikit-learn | Machine learning and preprocessing |
| Pandas       | Data processing                    |
| NumPy        | Numerical operations               |
| HTML/CSS     | Frontend interface                 |
| Gunicorn     | Production WSGI server             |
| Render       | Deployment                         |

---

## Machine Learning Workflow

The project follows a complete machine learning pipeline:

```text
Input Data
    ↓
Data Preprocessing
    ↓
Missing Value Handling
    ↓
Categorical Encoding
    ↓
Train/Test Split
    ↓
Feature Scaling
    ↓
Random Forest Training
    ↓
Model Evaluation
    ↓
Save Model & Scaler
    ↓
Flask Web Application
    ↓
User Input
    ↓
Prediction
```

---

## Dataset

The project currently uses a **synthetically generated dataset** for educational and reproducibility purposes.

The dataset follows the feature structure of the **Indian Liver Patient Dataset (ILPD)**, containing patient information and liver function test measurements.

Each record contains 10 input features:

* Age
* Gender
* Total Bilirubin
* Direct Bilirubin
* Alkaline Phosphotase
* Alamine Aminotransferase (ALT)
* Aspartate Aminotransferase (AST)
* Total Proteins
* Albumin
* Albumin and Globulin Ratio

The target variable represents whether the patient is classified as healthy or likely to have liver disease.

> The synthetic dataset does not represent real patient records and should not be interpreted as clinical data.

---

## Machine Learning Model

### Random Forest Classifier

The project uses a **Random Forest Classifier**.

Random Forest is an ensemble learning algorithm that combines predictions from multiple decision trees to produce a final classification.

### Why Random Forest?

It was selected because:

* It can model non-linear relationships.
* It generally performs better than a single decision tree.
* It is relatively robust to overfitting.
* It can provide feature importance.
* It works well for classification problems involving multiple numerical features.

---

## Data Preprocessing

Before training, the following preprocessing steps are performed:

### 1. Handling Missing Values

Missing numerical values are handled using the appropriate column statistics so that the model receives complete input data.

### 2. Gender Encoding

The categorical `Gender` feature is converted into a numerical representation because the machine learning model requires numerical inputs.

### 3. Train-Test Split

The dataset is divided into:

```text
80% → Training data
20% → Testing data
```

The training data is used to train the model, while the test data is kept separate for evaluating its performance.

### 4. Feature Scaling

`StandardScaler` is used to standardize the numerical features.

This transforms features to a comparable scale and ensures that features with larger numerical ranges do not dominate the preprocessing pipeline.

The scaler used during training is saved and reused when making predictions.

---

## Model Evaluation

The model is evaluated using the held-out test dataset.

The current implementation achieves approximately **97% accuracy on the test set**.

However, this result should **not** be interpreted as clinical-level performance because the current project uses synthetic data.

For a production or research-grade system, additional evaluation would be required, including:

* Cross-validation
* Precision
* Recall
* F1-score
* Confusion matrix
* ROC-AUC
* Class imbalance analysis
* Evaluation on an independent real-world dataset

In a healthcare prediction problem, **recall and false-negative rates are particularly important**, because incorrectly classifying a patient with liver disease as healthy could have serious consequences.

---

## Web Application

The Flask application provides a simple web interface.

### Prediction Flow

```text
User enters patient information
             ↓
       HTML form
             ↓
        Flask / app.py
             ↓
       Input validation
             ↓
   Previously saved scaler
             ↓
    Random Forest model
             ↓
       Prediction
             ↓
 Confidence + feature information
             ↓
       Result page
```

The trained model and scaler are loaded when the Flask application starts.

---

## Project Structure

```text
liver-disease-prediction/
│
├── app.py
├── generate_dataset.py
├── train_model.py
├── requirements.txt
├── dataset.csv
├── model.pkl
├── scaler.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

### File Description

| File                    | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| `generate_dataset.py`   | Generates the synthetic dataset                                       |
| `train_model.py`        | Preprocesses data, trains the model and saves the trained artifacts   |
| `app.py`                | Flask application responsible for handling user input and predictions |
| `templates/index.html`  | Patient input form                                                    |
| `templates/result.html` | Displays prediction results                                           |
| `static/style.css`      | Styling for the web application                                       |
| `dataset.csv`           | Generated dataset used for training                                   |
| `model.pkl`             | Saved trained Random Forest model                                     |
| `scaler.pkl`            | Saved feature scaler                                                  |
| `requirements.txt`      | Python dependencies                                                   |

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/saiprasanth-026/liver-disease-prediction.git
```

### 2. Navigate to the project

```bash
cd liver-disease-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the dataset

Run this only if `dataset.csv` is not already available:

```bash
python generate_dataset.py
```

### 5. Train the model

```bash
python train_model.py
```

This generates:

```text
model.pkl
scaler.pkl
```

### 6. Start the Flask application

```bash
python app.py
```

### 7. Open the application

Visit:

```text
http://127.0.0.1:5000
```

---

## Deployment on Render

The application can be deployed using **Render**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn --bind 0.0.0.0:$PORT app:app
```

### Deployment Requirements

Make sure the repository contains:

```text
model.pkl
scaler.pkl
requirements.txt
app.py
```

The saved model and scaler are required by the Flask application when it starts.

---

## GitHub Setup

Initialize Git in the project directory:

```bash
git init
```

Add the project files:

```bash
git add .
```

Create the first commit:

```bash
git commit -m "Initial liver disease prediction app"
```

Set the main branch:

```bash
git branch -M main
```

Connect the GitHub repository:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Push the project:

```bash
git push -u origin main
```

---

## Future Improvements

The project can be improved in several ways:

### Dataset

* Use a verified real-world dataset such as the original ILPD dataset.
* Increase the amount and diversity of training data.
* Perform more detailed data quality analysis.

### Machine Learning

* Compare multiple algorithms such as:

  * Logistic Regression
  * Decision Tree
  * Random Forest
  * XGBoost
  * Support Vector Machine
* Perform hyperparameter tuning.
* Use cross-validation.
* Evaluate precision, recall, F1-score and ROC-AUC.
* Analyze class imbalance.

### Web Application

* Add stronger input validation.
* Add better error handling.
* Improve UI/UX.
* Add prediction history.
* Add authentication if required.
* Provide clearer explanations of model predictions.

### Production

* Add automated testing.
* Use a proper database where appropriate.
* Containerize the application using Docker.
* Set up CI/CD.
* Add monitoring and logging.

---

## Interview Explanation

### 1. What problem does the project solve?

> "This project is an educational machine learning application that predicts whether a patient is likely to have liver disease based on liver function test parameters. The goal is to demonstrate an end-to-end machine learning workflow, from data preprocessing and model training to deployment through a Flask web application."

### 2. What technologies did you use?

> "I used Python for the implementation, Pandas and NumPy for data processing, Scikit-learn for preprocessing and machine learning, Flask for the web application, HTML and CSS for the frontend, and Gunicorn for production deployment."

### 3. Why did you choose Random Forest?

> "I chose Random Forest because it is an ensemble algorithm that combines multiple decision trees. It can capture non-linear relationships, is generally more robust than a single decision tree, and provides feature importance that can help with model interpretation."

### 4. What preprocessing did you perform?

> "I handled missing values, encoded the categorical gender feature into numerical form, split the dataset into training and testing sets, and standardized the features using StandardScaler."

### 5. How does prediction happen?

> "When the user submits the form, Flask receives the input values, converts them into the required numerical format, applies the same scaler that was fitted during training, and passes the transformed data to the saved Random Forest model. The model then returns the predicted class and confidence information, which Flask sends to the result page."

### 6. Why did you save `model.pkl` and `scaler.pkl`?

> "`model.pkl` contains the trained machine learning model, while `scaler.pkl` contains the scaler fitted during training. Saving them allows the application to reuse the trained model without retraining every time the Flask server starts. More importantly, using the same fitted scaler ensures that new inputs are transformed consistently with the training data."

### 7. How accurate is your model?

> "The current implementation achieves approximately 97% accuracy on the held-out test set. However, because the project uses synthetic data, I would not claim that this represents real clinical performance. A real healthcare application would require much more rigorous validation using real, independent clinical datasets."

### 8. What would you improve?

> "I would first use a verified real-world dataset and perform cross-validation. Then I would compare multiple models and evaluate metrics such as precision, recall, F1-score and ROC-AUC instead of relying only on accuracy. I would also improve input validation, error handling, testing, security and deployment."

---

## Disclaimer

This project is intended **only for educational and demonstration purposes**.

It is not a medical diagnostic system and must not be used to diagnose, treat, or make medical decisions about any individual.

The dataset used in this repository is synthetic and does not contain real patient information.
