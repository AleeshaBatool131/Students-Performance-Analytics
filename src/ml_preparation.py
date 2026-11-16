import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("outputs/students_cleaned.csv")
print("Orginal dataset")
print(df.head())
print("\nDataset shape: ", df.shape)

#select features (x)
x = df[
    [
    "Study_Hours",
    "Attendance",
    "Previous_Marks"
    ]
]
# select target(y)
y = df["Final_Marks"]
print("\nFeatures (x)")
print(x.head())
print("\nFeatures shape: ", x.shape)
print("\nTarget(y)")
print(y.head())
print("\nTarget shape: ", y.shape)

#splitting data into training and testing
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.20, #20% of records are reserved for testing
    random_state=42 # makes the split reproducible
)
print("\nTraining Data")
print("X_train shape: ", x_train.shape)
print("y_train shape: ", y_train.shape)

print("\nTesting Data")
print("X_test shape: ", x_test.shape)
print("y_test shape: ", y_test.shape)