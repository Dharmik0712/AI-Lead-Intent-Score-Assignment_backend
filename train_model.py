import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os
import json

# Load the dataset
df = pd.read_csv("data/leads.csv")

# Drop irrelevant columns
drop_cols = ["lead_id", "name", "email", "phone_number", "lead_created_at"]
X = df.drop(columns=drop_cols + ["intent_score"], errors="ignore")
y = df["intent_score"]

# One-hot encoding for categorical variables
X = pd.get_dummies(X)

# Clean column names (spaces, symbols)
X.columns = [col.replace('[', '').replace(']', '').replace('<', '').replace('>', '').replace(' ', '_') for col in X.columns]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost regressor
model = xgb.XGBRegressor(n_estimators=100, max_depth=5, learning_rate=0.1, objective="reg:squarederror")
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"✅ Model trained. MSE: {mse:.2f}, R²: {r2:.2f}")

# Save the model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/lead_score_model.pkl")

# Save feature columns
with open("model/feature_columns.json", "w") as f:
    json.dump(X.columns.tolist(), f)

print("✅ Model and features saved.")
