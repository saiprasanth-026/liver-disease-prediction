# Liver Disease Prediction System

An end-to-end machine learning web application that predicts whether a patient is **likely to have liver disease** based on liver function test results.

The application uses **Python, Scikit-learn, and Flask** to provide a simple web interface where users can enter patient parameters and receive a prediction with a confidence score.

> **Disclaimer:** This is an educational machine learning project. It is not a medical diagnostic tool and should not be used for clinical decision-making.

## 🚀 Live Demo

**[Liver Disease Prediction System](https://liver-disease-prediction-1sae.onrender.com)**

The application is deployed on Render and can be accessed directly through the link above.

> **Note:** Since the application is hosted on a free-tier service, the first request may take a little longer if the service has been inactive.

---

## ✨ Features

* Predicts **Healthy** or **Liver Disease Likely**
* Accepts 10 patient-related features
* Handles data preprocessing
* Uses a **Random Forest Classifier**
* Uses `StandardScaler` for feature scaling
* Displays prediction confidence
* Displays top contributing features
* Simple Flask-based web interface
* Deployed as a publicly accessible web application
* Source code available on GitHub

---

## 🛠️ Technologies Used

| Technology   | Purpose                                 |
| ------------ | --------------------------------------- |
| Python       | Core programming language               |
| Flask        | Web application framework               |
| Scikit-learn | Machine learning and preprocessing      |
| Pandas       | Data processing                         |
| NumPy        | Numerical operations                    |
| HTML         | Web page structure                      |
| CSS          | User interface styling                  |
| Gunicorn     | Production WSGI server                  |
| Render       | Cloud deployment                        |
| Git & GitHub | Version control and source-code hosting |

---

## 🧠 Machine Learning Workflow

The project follows a complete machine learning pipeline:

```text
Patient Dataset
      ↓
Data Preprocessing
      ↓
Missing Value Handling
      ↓
Gender Encoding
      ↓
Train-Test Split
      ↓
Feature Scaling
      ↓
Random Forest Training
      ↓
Model Evaluation
      ↓
Save Trained Model
      ↓
Flask Web Application
      ↓
User Input
      ↓
Prediction
      ↓
Result + Confidence
```

---

## 📊 Dataset

The project currently uses a **synthetically generated dataset** for educational and reproducibility purposes.

The dataset follows the feature structure of the **Indian Liver Patient Dataset (ILPD)**.

Each record contains the following 10 input features:

1. Age
2. Gender
3. Total Bilirubin
4. Direct Bilirubin
5. Alkaline Phosphotase
6. Alamine Aminotransferase (ALT)
7. Aspartate Aminotransferase (AST)
8. Total Proteins
9. Albumin
10. Albumin and Globulin Ratio

The target variable represents whether the patient is classified as:

* Healthy
* Liver Disease Likely

> The dataset used in this repository is synthetic and does not contain real patient information.

---

## 🤖 Machine Learning Model

### Random Forest Classifier

The project uses a **Random Forest Classifier** for prediction.

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to make a final prediction.

### Why Random Forest?

Random Forest was selected because:

* It can model non-linear relationships.
* It combines multiple decision trees.
* It is generally more robust than a single decision tree.
* It can reduce overfitting compared with an individual decision tree.
* It provides feature importance.
* It works well for classification problems.

---

## 🔄 Data Preprocessing

The following preprocessing steps are performed before training the model.

### 1. Missing Value Handling

Missing numerical values are handled using appropriate column statistics so that the machine learning model receives complete input data.

### 2. Gender Encoding

The `Gender` column contains categorical values such as Male and Female.

These values are converted into numerical representations because the machine learning model requires numerical input.

### 3. Train-Test Split

The dataset is divided into:

```text
80% → Training Data
20% → Testing Data
```

The training data is used to train the model, while the testing data is used to evaluate its performance on unseen data.

### 4. Feature Scaling

`StandardScaler` from Scikit-learn is used to standardize the numerical features.

This helps put features with different numerical ranges on a comparable scale.

The scaler fitted during training is saved as `scaler.pkl` and reused during prediction.

---

## 📈 Model Performance

The current implementation achieves approximately **97% accuracy on the held-out test set**.

However, this result should not be interpreted as clinical-level performance because the project uses a synthetic dataset.

For a real-world healthcare machine learning system, more rigorous evaluation would be required, including:

* Cross-validation
* Precision
* Recall
* F1-score
* Confusion matrix
* ROC-AUC
* Class imbalance analysis
* Evaluation using an independent real-world dataset

In a healthcare prediction problem, recall and false-negative rates are especially important because incorrectly classifying a patient with liver disease as healthy could have serious consequences.

---

## 🌐 Web Application

The application is built using **Flask**.

The user enters patient information through the web interface.

### Prediction Flow

```text
User enters patient information
             ↓
        HTML Form
             ↓
        Flask / app.py
             ↓
       Input Processing
             ↓
    Saved StandardScaler
             ↓
    Random Forest Model
             ↓
         Prediction
             ↓
 Confidence + Feature Information
             ↓
        Result Page
```

The trained model and scaler are loaded when the Flask application starts.

---

## 📁 Project Structure

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

| File                    | Purpose                                                                     |
| ----------------------- | --------------------------------------------------------------------------- |
| `app.py`                | Flask server that handles user input and predictions                        |
| `generate_dataset.py`   | Generates the synthetic dataset                                             |
| `train_model.py`        | Preprocesses data, trains the Random Forest model and saves model artifacts |
| `requirements.txt`      | Contains required Python dependencies                                       |
| `dataset.csv`           | Generated dataset used for model training                                   |
| `model.pkl`             | Saved trained Random Forest model                                           |
| `scaler.pkl`            | Saved feature scaler                                                        |
| `templates/index.html`  | Patient input form                                                          |
| `templates/result.html` | Displays prediction results                                                 |
| `static/style.css`      | Styling for the web application                                             |

---

## 💻 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/saiprasanth-026/liver-disease-prediction.git
```

### 2. Navigate to the Project

```bash
cd liver-disease-prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the Dataset

Run this only if `dataset.csv` is not already available:

```bash
python generate_dataset.py
```

### 5. Train the Model

```bash
python train_model.py
```

This generates the trained model and scaler:

```text
model.pkl
scaler.pkl
```

### 6. Start the Flask Application

```bash
python app.py
```

### 7. Open in Browser

Visit:

```text
http://127.0.0.1:5000
```

---

## ☁️ Deployment on Render

The application is deployed using **Render**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn --bind 0.0.0.0:$PORT app:app
```

### Required Files

The deployed application requires:

```text
app.py
requirements.txt
model.pkl
scaler.pkl
templates/
static/
```

The saved model and scaler are loaded by Flask when the application starts.

### Live Application

**https://liver-disease-prediction-1sae.onrender.com**

---

## 🔗 GitHub Repository

The complete source code is available on GitHub:

**https://github.com/saiprasanth-026/liver-disease-prediction**

---

## 📤 Push the Project to GitHub

If you want to push the project from your local VS Code environment:

### Initialize Git

```bash
git init
```

### Add Files

```bash
git add .
```

### Commit Changes

```bash
git commit -m "Initial liver disease prediction app"
```

### Set Main Branch

```bash
git branch -M main
```

### Connect GitHub Repository

```bash
git remote add origin https://github.com/saiprasanth-026/liver-disease-prediction.git
```

### Push to GitHub

```bash
git push -u origin main
```

For future changes:

```bash
git add .
git commit -m "Update project"
git push
```

---

## 🔮 Future Improvements

### Dataset Improvements

* Use a verified real-world liver disease dataset.
* Increase dataset size and diversity.
* Perform detailed exploratory data analysis.
* Handle class imbalance appropriately.

### Machine Learning Improvements

* Compare multiple algorithms:

  * Logistic Regression
  * Decision Tree
  * Random Forest
  * Support Vector Machine
  * XGBoost
* Perform hyperparameter tuning.
* Use cross-validation.
* Evaluate precision, recall, F1-score and ROC-AUC.
* Analyze feature importance.
* Improve model interpretability.

### Web Application Improvements

* Add stronger input validation.
* Add better error handling.
* Improve UI/UX.
* Add prediction history.
* Add authentication if required.
* Provide clearer explanations of predictions.

### Deployment Improvements

* Add automated testing.
* Add application logging and monitoring.
* Containerize the application using Docker.
* Set up CI/CD.
* Use a database for storing application data where appropriate.

---

## 🎯 Interview Explanation

### 1. What problem does the project solve?

> "This project is an educational machine learning application that predicts whether a patient is likely to have liver disease based on liver function test parameters. The main goal was to implement an end-to-end machine learning workflow, from data preprocessing and model training to deployment through a Flask web application."

### 2. What technologies did you use?

> "I used Python for the implementation, Pandas and NumPy for data processing, Scikit-learn for preprocessing and machine learning, Flask for the web application, HTML and CSS for the frontend, Gunicorn as the production WSGI server, and Render for deployment."

### 3. Why did you choose Random Forest?

> "I chose Random Forest because it is an ensemble algorithm that combines multiple decision trees. It can capture non-linear relationships, is generally more robust than a single decision tree, and provides feature importance which can help with model interpretation."

### 4. What preprocessing did you perform?

> "I handled missing values, encoded the categorical gender feature into numerical form, split the dataset into training and testing sets, and standardized the features using StandardScaler."

### 5. Why did you use StandardScaler?

> "The features have different numerical ranges. For example, some liver enzyme values can be much larger than protein measurements. StandardScaler transforms the features into a comparable scale. I saved the fitted scaler and reused the same scaler during prediction so that new inputs are processed consistently with the training data."

### 6. Why did you save `model.pkl` and `scaler.pkl`?

> "`model.pkl` contains the trained Random Forest model, while `scaler.pkl` contains the scaler fitted on the training data. Saving them allows the Flask application to make predictions using the already-trained model without retraining it every time the application starts."

### 7. How does the application make a prediction?

> "The user enters the required patient parameters through the HTML form. Flask receives those values, converts them into the required format, applies the saved StandardScaler, and passes the transformed data to the trained Random Forest model. The model returns the prediction, which Flask sends to the result page."

### 8. How accurate is your model?

> "The current implementation achieves approximately 97% accuracy on the held-out test set. However, the dataset is synthetic, so I would not claim that this represents real clinical performance. For a real application, I would use a verified real-world dataset and perform more rigorous validation."

### 9. What would you improve?

> "I would use a verified real-world dataset, perform cross-validation, compare multiple machine learning algorithms, tune the model hyperparameters, evaluate metrics such as precision, recall, F1-score and ROC-AUC, and improve validation, error handling, security and testing in the web application."

---

## ⚠️ Disclaimer

This project is intended **only for educational and demonstration purposes**.

It is **not a medical diagnostic system** and must not be used to diagnose, treat, or make medical decisions about any individual.

The dataset used in this repository is synthetic and does not contain real patient information.

---

## 👨‍💻 Project Links

**Live Demo:**
https://liver-disease-prediction-1sae.onrender.com

**GitHub Repository:**
https://github.com/saiprasanth-026/liver-disease-prediction
