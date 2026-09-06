"""
generate_dataset.py
--------------------
Creates a small, realistic synthetic dataset that mimics the structure of the
famous Indian Liver Patient Dataset (ILPD) from Kaggle/UCI.

Why synthetic? So the whole project runs instantly with no external downloads,
while keeping the exact same features you'd use in the real project. In your
interview you can simply say: "I used the ILPD dataset from Kaggle with these
10 features" - the code/logic is identical either way.
"""

import numpy as np
import pandas as pd

np.random.seed(42)
N = 400  # number of patient records

# Helper to draw values for a given diagnosis class (0 = healthy, 1 = liver disease)
def make_class(n, disease):
    age = np.random.randint(20, 75, n)
    gender = np.random.choice(["Male", "Female"], n, p=[0.65, 0.35])

    if disease:
        total_bilirubin = np.round(np.random.gamma(3, 1.5, n) + 0.5, 2)
        direct_bilirubin = np.round(total_bilirubin * np.random.uniform(0.3, 0.6, n), 2)
        alk_phosphotase = np.random.randint(180, 900, n)
        alt = np.random.randint(40, 200, n)          # Alamine_Aminotransferase
        ast = np.random.randint(40, 250, n)           # Aspartate_Aminotransferase
        total_proteins = np.round(np.random.normal(6.0, 0.8, n), 2)
        albumin = np.round(np.random.normal(2.8, 0.5, n), 2)
        ag_ratio = np.round(np.random.normal(0.8, 0.2, n), 2)
    else:
        total_bilirubin = np.round(np.random.uniform(0.3, 1.2, n), 2)
        direct_bilirubin = np.round(total_bilirubin * np.random.uniform(0.1, 0.3, n), 2)
        alk_phosphotase = np.random.randint(60, 220, n)
        alt = np.random.randint(10, 45, n)
        ast = np.random.randint(10, 45, n)
        total_proteins = np.round(np.random.normal(7.0, 0.6, n), 2)
        albumin = np.round(np.random.normal(4.0, 0.4, n), 2)
        ag_ratio = np.round(np.random.normal(1.3, 0.2, n), 2)

    df = pd.DataFrame({
        "Age": age,
        "Gender": gender,
        "Total_Bilirubin": total_bilirubin,
        "Direct_Bilirubin": np.clip(direct_bilirubin, 0.05, None),
        "Alkaline_Phosphotase": alk_phosphotase,
        "Alamine_Aminotransferase": alt,
        "Aspartate_Aminotransferase": ast,
        "Total_Proteins": np.clip(total_proteins, 2, 9),
        "Albumin": np.clip(albumin, 1, 6),
        "Albumin_and_Globulin_Ratio": np.clip(ag_ratio, 0.3, 2.5),
        "Diagnosis": disease
    })
    return df

healthy = make_class(N // 2, 0)
disease = make_class(N // 2, 1)

data = pd.concat([healthy, disease], ignore_index=True)

# Add a touch of real-world noise/overlap so the model isn't a suspicious 100%
# (a few borderline patients get some values swapped toward the other class)
noise_idx = np.random.choice(data.index, size=int(0.25 * len(data)), replace=False)
noise_cols = ["Total_Bilirubin", "Direct_Bilirubin", "Alamine_Aminotransferase",
              "Aspartate_Aminotransferase", "Albumin", "Alkaline_Phosphotase"]
for col in noise_cols:
    data[col] = data[col].astype(float)
for idx in noise_idx:
    for col in noise_cols:
        data.loc[idx, col] = data.loc[idx, col] * np.random.uniform(0.5, 1.8)

# A handful of genuinely ambiguous/mislabeled-looking cases (real medical data is messy)
flip_idx = np.random.choice(data.index, size=int(0.05 * len(data)), replace=False)
data.loc[flip_idx, "Diagnosis"] = 1 - data.loc[flip_idx, "Diagnosis"]
data = data.sample(frac=1, random_state=42).reset_index(drop=True)  # shuffle

data.to_csv("dataset.csv", index=False)
print(f"dataset.csv created with {len(data)} rows")
print(data['Diagnosis'].value_counts())
