from pathlib import Path
import joblib   # to save the trained model
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

df = pd.read_csv("outputs/students_cleaned.csv")
X = df[["Study_Hours", "Attendance", "Previous_Marks"]]
y = df["Final_Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# evaluating the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel evaluation")
print("Mean Absolute error (MAE): ", mae)
print("Mean Squared Error (MSE): ", mse)
print("Root Mean Squared Error (RMSE): ", rmse)
print("R2 Score: ", round(r2, 4))

# comparing actual and predicted marks
results = pd.DataFrame({     # creates the table containing: 
    "Student_ID": df.loc[X_test.index, "Student_ID"].values,
    "Actual_Marks": y_test.values,
    "Predicted_Marks": y_pred.round(2)
})

results["Error"] = (
    results["Actual_Marks"] - results["Predicted_Marks"]
).round(2)

results["Absolute_Error"] = results["Error"].abs() # converts negative errors into positive values
print("\nActual vs Predicted ")
print(results.to_string(index=False))

# Visualization
plt.figure(figsize=(8,6))
plt.scatter(
    y_test,
    y_pred,
    s = 80,
    label = "Student Predictions"
)
# ideal prediction reference line
minimum = min(y_test.min(), y_pred.min())
maximum = max(y_test.max(), y_pred.max())

plt.plot(
    [minimum, maximum],
    [minimum, maximum],
    linestyle="--",
    label = "Perfect Prediction"
)

plt.xlabel("Actual Final Marks")
plt.ylabel("Predicted Final Marks")
plt.title("Actual vs Predicted final Marks")

plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

Path("outputs").mkdir(exist_ok=True)
plt.savefig(
    "outputs/model_evaluation.png",
    dpi = 300,
    bbox_inches= "tight"
)
plt.show()
print("\nEvaluation graph saved successfully.")

# saving the trained model
model_path = "outputs/linear_regression_model.pkl"  # .pkl stores python object
joblib.dump(model, model_path)
print("Model saved")
print("Model location: ", model_path)

loaded_model = joblib.load(model_path)
print("MOdel loaded")

new_student = pd.DataFrame({
    "Study_Hours": [6], 
    "Attendance": [90],
    "Previous_Marks": [80]
})
new_prediction = loaded_model.predict(new_student)

print("\n========== NEW STUDENT PREDICTION ==========")
print("Study Hours: 6")
print("Attendance: 90%")
print("Previous Marks: 80")
print("Predicted Final Marks:", round(new_prediction[0], 2))