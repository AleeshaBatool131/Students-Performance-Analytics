 # Complete Workflow
from pathlib import Path
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import(
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
DATA_PATH = Path("data/students_raw.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)
FEATURES = [
    "Study_Hours",
    "Attendance",
    "Previous_Marks"
]
TARGET = "Final_Marks"
NUMERIC_COLUMNS = FEATURES + [TARGET]
print("\n========= Student Performance Analytics =======")
if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_PATH}"
    )
df = pd.read_csv(DATA_PATH)
print("\nOriginal Dataset")
print(df.head())
print("Original Records: ", len(df))

print("\nData cleaning")
df.columns = df.columns.str.strip() # remove unnecessary spaces from columns' names
required_columns = ["Student_ID"] + NUMERIC_COLUMNS
missing_columns = [
    column for column in required_columns
    if column not in df.columns
]
if missing_columns:
    raise ValueError(
        f"Required columns are missing: {missing_columns}"
    )
df["Student_ID"] = df["Student_ID"].astype("string").str.strip()
for column in NUMERIC_COLUMNS:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

df = df.dropna(subset=["Student_ID"])
df = df[df["Student_ID"] != ""]
df = df.drop_duplicates()
df = df.drop_duplicates(
    subset=["Student_ID"],
    keep="first"
)
df.loc[
    ~df["Study_Hours"].between(0,24),
    "Study_Hours"
] = float("nan")
df.loc[
    ~df["Attendance"].between(0,100),
    "Attendance"
] = float("nan")
df.loc[
    ~df["Previous_Marks"].between(0,100),
    "Previous_Marks"
]=float("nan")
df.loc[
    ~df["Final_Marks"].between(0,100),
    "Final_Marks"
] = float("nan")

df = df.dropna(subset=[TARGET])
df = df.reset_index(drop=True)

print("Records after cleaning: ", len(df))
print("\nMissing values after cleaning: ")
print(df[NUMERIC_COLUMNS].isnull().sum())
df.to_csv(
    OUTPUT_DIR/"students_cleaned.csv",
    index = False
)
print("Cleaned dataset saved successfully.")

X = df[FEATURES]
y = df[TARGET]
print("\nFeature Selection")
print("\nINput Features")
print(FEATURES)
print("\nTarget variable:")
print(TARGET)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    train_size=0.20,
    random_state=42
)
print("\n========== DATA SPLITTING ==========")

print("Training records:", len(X_train))
print("Testing records:", len(X_test))
# preprocessing and model pipeline
#Pipeline connects multiple machine learning operations into one workflow.
model = Pipeline(steps=[
    (
        "imputer",
        SimpleImputer(strategy="median") # fills missing feature values using training medians
    ),
    (
        "regression",
        LinearRegression()
    )
])
print("\nPipeline created")
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

r2 = r2_score(y_test, y_pred)

print("\n========== MODEL EVALUATION ==========")

print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))
results = pd.DataFrame({
    "Student_ID": df.loc[X_test.index, "Student_ID"].values,
    "Actual_Marks": y_test.values,
    "Predicted_Marks": y_pred.round(2)
})

results["Error"] = (
    results["Actual_Marks"] -
    results["Predicted_Marks"]
).round(2)

results["Absolute_Error"] = results["Error"].abs()

print("\n========== PREDICTION RESULTS ==========")

print(results.to_string(index=False))

# Save prediction results
results.to_csv(
    OUTPUT_DIR / "test_predictions.csv",
    index=False
)

print("\nPrediction results saved successfully.")

plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    y_pred,
    s=80,
    label="Predicted Students"
)

minimum = min(y_test.min(), y_pred.min())
maximum = max(y_test.max(), y_pred.max())

plt.plot(
    [minimum, maximum],
    [minimum, maximum],
    linestyle="--",
    label="Perfect Prediction"
)

plt.xlabel("Actual Final Marks")
plt.ylabel("Predicted Final Marks")

plt.title("Student Performance: Actual vs Predicted")

plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "model_evaluation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nEvaluation graph saved successfully.")

regression_model = model.named_steps["regression"]

print("\n========== MODEL PARAMETERS ==========")

print("Intercept:", round(regression_model.intercept_, 4))

for feature, coefficient in zip(
    FEATURES,
    regression_model.coef_
):
    print(
        f"{feature} coefficient: {coefficient:.4f}"
    )

model_path = OUTPUT_DIR / "student_performance_model.joblib"

joblib.dump(model, model_path)

print("\n========== MODEL SAVED ==========")

print("Saved location:", model_path)

loaded_model = joblib.load(model_path)

print("\nSaved model loaded successfully.")

new_student = pd.DataFrame({
    "Study_Hours": [6],
    "Attendance": [90],
    "Previous_Marks": [80]
})

new_prediction = loaded_model.predict(new_student)

print("\n========== NEW STUDENT PREDICTION ==========")

print("Study Hours:", new_student.iloc[0]["Study_Hours"])
print("Attendance:", new_student.iloc[0]["Attendance"])
print("Previous Marks:", new_student.iloc[0]["Previous_Marks"])

print(
    "Predicted Final Marks:",
    round(new_prediction[0], 2)
)

print("\n========== PROJECT COMPLETED ==========")

print("Student Performance Analytics System executed successfully.")
