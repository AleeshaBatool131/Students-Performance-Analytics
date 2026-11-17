
# Student Performance Analytics System

A beginner-friendly Python data analytics and machine learning project that explores student performance using study hours, attendance, previous marks, and final marks.

## Project Overview

The goal of this project is to analyse student data, understand the factors associated with academic performance, clean and prepare the dataset, and later build a machine learning model to predict students' final marks.

The project is being developed in **Python** using **VS Code**. Pandas is used for data manipulation, while Matplotlib and Seaborn are used for visualisation.
## Technologies and Libraries

- **Python** — main programming language.
- **Pandas** — loading, inspecting, analysing, and cleaning tabular data.
- **Matplotlib** — creating charts.
- **Seaborn** — creating statistical visualisations.
- **VS Code** — development environment.


## Work Completed So Far

### Milestone 1 — Python Environment and Project Setup

- Set up the project in Visual Studio Code.
- Created and used a Python virtual environment (`venv`).
- Installed the required Python libraries.
- Created an organised project folder structure.

### Milestone 2 — Data Analysis with Pandas

- Loaded the student dataset from a CSV file using Pandas.
- Inspected the dataset using `head()`, `tail()`, `shape`, and `columns`.
- Generated descriptive statistics using `describe()`.
- Calculated average values, including average final marks.
- Counted students and calculated average study hours and attendance.
- Identified the highest final mark.
- Filtered students who scored 80 or above.

### Milestone 3 — Data Visualisation

Created a student performance dashboard containing:

- A histogram showing the distribution of final marks.
- A scatter plot showing the relationship between study hours and final marks.
- A scatter plot comparing previous marks with final marks.
- A correlation heatmap for the numerical columns.

The dashboard is saved in the `outputs` folder.

### Milestone 4 — Data Cleaning and Preprocessing

- Created a separate practice dataset, `students_raw.csv`, containing intentional data-quality issues.
- Removed extra spaces from column names and student IDs.
- Converted numeric columns to numeric data types.
- Identified missing values.
- Detected and removed duplicate records.
- Checked for duplicate student IDs.
- Identified invalid values, such as negative marks, study hours above 24, attendance above 100, and marks above 100.
- Replaced invalid values with missing values.
- Filled missing predictor values using the median.
- Removed rows where the target value (`Final_Marks`) was missing.
- Reset the DataFrame index after cleaning.
- Exported the cleaned dataset to `outputs/students_cleaned.csv`.

**Note:** The cleaning rules assume study hours are between 0 and 24, and attendance and marks are percentages between 0 and 100. These limits should be adjusted if the dataset uses different definitions. The practice dataset is kept separate so the original `students.csv` remains unchanged.


### Milestone 5 — Exploratory Data Analysis (EDA)

- Explored the cleaned student dataset using Pandas.
- Examined dataset dimensions, columns, data types, and descriptive statistics.
- Analysed mean, median, minimum, maximum, and standard deviation of student marks.
- Investigated correlations between study hours, attendance, previous marks, and final marks.
- Compared average final marks according to study hours and attendance.
- Detected potential outliers using the Interquartile Range (IQR) method.
- Created an EDA dashboard using Matplotlib and Seaborn.
- Saved the dashboard as `outputs/eda_dashboard.png`.
### Milestone 6 — Introduction to Machine Learning

- Learned the fundamentals of Machine Learning.
- Studied supervised, unsupervised, and reinforcement learning.
- Understood important ML concepts, including features, targets, training, testing, models, and predictions.
- Learned the basic concepts of Linear Regression.
- Installed the Scikit-learn library.
- Selected input features (`Study_Hours`, `Attendance`, and `Previous_Marks`).
- Selected `Final_Marks` as the target variable.
- Divided the dataset into training and testing sets using `train_test_split()`.
- Prepared the dataset for the first Machine Learning model.
### Milestone 7 — First Machine Learning Model: Linear Regression

- Learned the fundamentals of Linear Regression.
- Understood simple and multiple linear regression equations.
- Imported the Linear Regression algorithm from Scikit-learn.
- Created a Linear Regression model using `LinearRegression()`.
- Trained the model using `fit()`.
- Examined the learned coefficients and intercept.
- Generated predictions using `predict()`.
- Predicted final marks for a new student using study hours, attendance, and previous marks.

*This is an educational project developed incrementally while learning Python, data analysis, and machine learning.*
