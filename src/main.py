import pandas as pd
df = pd.read_csv("data/students.csv") #DataFrame
print("First Five Students: ")
print(df.head())
print("\nLast Five Students: ")
print(df.tail())
print("\nDataSet Dimension: ")
print(df.shape)
print("\nColumns Name: ")
print(df.columns)
print("\nStatistical Summary: ")
print(df.describe())
print("\nAverage Final Marks:")
print(df["Final_Marks"].mean())