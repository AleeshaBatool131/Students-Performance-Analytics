import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("outputs/students_cleaned.csv")
print("Dataset Loaded")
print(df.head())
print("\nTotal Records: ", len(df))

X = df[
    [
        "Study_Hours",
        "Attendance",
        "Previous_Marks"
    ]
]
y = df["Final_Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
print("\nData Splitting")
print("Training Records: ", len(X_train))
print("Testing records: ", len(X_test))

# creating model
model = LinearRegression()

model.fit(X_train, y_train)

print("\n model trained successfully")

# model coefficients
print("\nModel Parameters")
print("Intercept: ", model.intercept_)
#The coefficients represent the estimated contribution of each feature to the prediction, holding the other features constant.

#For example, if the study-hours coefficient is positive, the model estimates that increasing study hours is associated with an increase in predicted marks, assuming other features stay the same.
for feature, coefficient in zip(X.columns, model.coef_):
    print(f"{feature} coefficient: {coefficient}")
# predictions on testing data
y_predictions = model.predict(X_test)
results = pd.DataFrame({
    "Actual_Marks": y_test.values,
    "Predicted_Marks": y_predictions.round(2)
})
print("\nSample Test Predictions")
print(results)

# predict marks for new student
new_student = pd.DataFrame({
    "Study_Hours": [6],
    "Attendance": [90],
    "Previous_Marks": [80]
})

predicted_marks = model.predict(new_student)
print("\nNew student Prediction")
print("Study Hours: 6")
print("Attendance: 90")
print("Previous Marks: 80")
print("Predicted Final Marks: ", round(predicted_marks[0], 2))
print("\n Linear Regression Completed.")