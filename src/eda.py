import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

df = pd.read_csv("outputs/students_cleaned.csv")
print("Dataset Overview")
print("\nFirst five records:")
print(df.head())
print("\nDataset shape: ")
print(df.shape)
print("\nColumn names: ")
print(df.columns.to_list())
print("\nDataset Information:")
df.info()

# Descriptive statistics
print("\nDescriptive STATistics")
print(df.describe())
print("\nAverage values: ")
print(df.mean(numeric_only=True))
print("\nMedian values: ")
print(df.median(numeric_only=True))

# Analyse final marks:
print("\nFinal Marks Analysis")
print("Average final marks: ", df["Final_Marks"].mean())
print("Median final marks: ", df["Final_Marks"].median())
print("Highest final marks: ", df["Final_Marks"].max())
print("Lowest final marks: ", df["Final_Marks"].min())
print("Standard deviation: ", df["Final_Marks"].std())

print("\nCorrelation Matrix")
correlation = df.select_dtypes(include="number").corr()
print(correlation)
print("\nCorrelation with Final Marks:")
print(correlation["Final_Marks"].sort_values(ascending=False))

print("\nGroup Analysis")
#average final marks accroding to study hours
study_group = (
    df.groupby("Study_Hours")["Final_Marks"]
    .mean()
    .sort_index
)
print("Average final marks by study hours: ")
print(study_group)
attendance_group = (
    df.groupby("Attendance")["Final_Marks"]
    .mean()
    .sort_index()
)
print("Average final marks by attendance:")
print(attendance_group)

print("\nOutlier Detection")
numeric_columns = [
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Final_Marks"
]
for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3-Q1 #InterQuartile Range
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column]< lower_limit) | 
        (df[column] > upper_limit)
    ]
    print(f"\n{column}")
    print("Lower limit: ", lower_limit)
    print("Upper limit: ", upper_limit)
    print("Number of potential outliers: ", len(outliers))

# creating eda visualization dashboard
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 3, figsize = (18, 10))
sns.histplot(
    data=df,
    x="Final_Marks",
    bins=10,
    kde=True,
    ax=axes[0,0]
)
axes[0,0].set_title("Distribution of Final Marks")

sns.boxplot(
    data=df,
    y="Final_Marks",
    ax = axes[0,1]
)
axes[0,1].set_title("Final Marks - Boxplot")

sns.scatterplot(
    data=df,
    x = "Study_Hours",
    y="Final_Marks",
    ax=axes[0,2]
)
axes[0,2].set_title("Study Hours vs Final Marks")

sns.scatterplot(
    data=df,
    x = "Attendance",
    y="Final_Marks",
    ax=axes[1,0]
)
axes[1,0].set_title("Attendance vs Final Marks")

sns.scatterplot(
    data=df,
    x = "Previous_Marks",
    y="Final_Marks",
    ax=axes[1,1]
)
axes[1,1].set_title("Previous Marks vs Final Marks")

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    ax = axes[1,2]
)
axes[1,2].set_title("Correlation Heatmap")
plt.tight_layout()

Path("outputs").mkdir(exist_ok=True)
plt.savefig(
    "outputs/eda_dashboard.png",
    dpi = 300,
    bbox_inches = "tight"
)

print("\nEDA dashboard saved successfully!")
print("Location: outputs/eda_dashboard.png")
plt.show()