# Data Cleaning and Preprocessing
import pandas as pd
from pathlib import  Path

df = pd.read_csv("data/students_raw.csv")
print("======== Original Dataset =========")
print(df.head())
print("\nOriginal dataset shape: ", df.shape)

#Standardizing the columns names
df.columns = df.columns.str.strip()
# removing unnecessary spaces from Student_ID
df["Student_ID"] = df["Student_ID"].astype("string").str.strip()
df["Student_ID"] = df["Student_ID"].replace("", pd.NA)

# converting numerical columns to numeric types
numeric_columns = [
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Final_Marks"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce" #instead of stopping the program with an error, errors="coerce" converts it into a missing value (NaN).
    )

print("\n====== Missing Values ======")
print(df.isnull().sum())

df = df.dropna(subset=["Student_ID"]) # remove rows

duplicate_count = df.duplicated().sum()
print("\nDuplicate records found: ", duplicate_count)
df = df.drop_duplicates() # remove exact duplicate records

# remove duplicate studentId records
duplicate_id_count = df["Student_ID"].duplicated().sum()
print("Duplicate Student ID found: ", duplicate_id_count)
df = df.drop_duplicates(subset=["Student_ID"], keep="first")

#handling invalid study hours
df.loc[
    (df["Study_Hours"] < 0) |
    (df["Study_Hours"] > 24),
    "Study_Hours"
] = pd.NA

# invalid attendance

df.loc[
    (df["Attendance"]<0) |
    (df["Attendance"] > 100),
    "Attendance"
] = pd.NA

# invalid previous marks
df.loc[
    (df["Previous_Marks"] < 0) |
    (df["Previous_Marks"] > 100),
    "Previous_Marks"
] = pd.NA
# invalid final marks
df.loc[
    (df["Final_Marks"] < 0) |
    (df["Final_Marks"] > 100),
    "Final_Marks"
] = pd.NA

# filling missing predictor values with median
predictor_columns = [
    "Study_Hours",
    "Attendance",
    "Previous_Marks"
]
for column in predictor_columns:
    median_value = df[column].median()
    if pd.notna(median_value):
        df[column] = df[column].fillna(median_value)

# remove records without valid final marks
df = df.dropna(subset=["Final_Marks"])

# reset index
df = df.reset_index(drop=True)

print("\n=== cleaned dataset ====")
print(df.head())
print("\nCleaned dataset shape: ", df.shape)

print("\n Remaining missing values: ")
print(df.isnull().sum())

Path("outputs").mkdir(exist_ok=True)
df.to_csv(
    "outputs/students_cleaned.csv",
    index = False
)

print("\n========== PREPROCESSING COMPLETED ==========")

print("Original records:", pd.read_csv("data/students_raw.csv").shape[0])

print("Cleaned records:", len(df))

print("Cleaned dataset saved successfully!")

print("Location: outputs/students_cleaned.csv")