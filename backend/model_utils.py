import joblib
import pandas as pd
import json

# Load trained model and feature columns
model = joblib.load("../model/lead_score_model.pkl")
with open("../model/feature_columns.json") as f:
    feature_cols = json.load(f)

def preprocess(lead: dict) -> pd.DataFrame:
    df = pd.DataFrame([lead])
    df = pd.get_dummies(df)

    for col in feature_cols:
        if col not in df.columns:
            df[col] = 0

    df = df[feature_cols]
    return df

def predict(lead: dict) -> int:
    X = preprocess(lead)
    score = model.predict(X)[0]
    return int(round(min(max(score, 0), 100)))  # Scale and clamp to 0–100
