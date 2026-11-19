
# Student Performance Analytics System

A beginner-friendly Python data analytics and machine learning project that explores student performance using study hours, attendance, previous marks, and final marks.

## Project Overview

The **Student Performance Analytics System** is designed to analyse student data, identify patterns associated with academic performance, clean and prepare datasets, and build a machine learning model to predict students' final marks.

The project follows an end-to-end data science workflow, starting with data collection and preprocessing and ending with model training, evaluation, and prediction.

It is developed using **Python** in **Visual Studio Code (VS Code)**.

## Technologies and Libraries

- **Python** — Main programming language.
- **Pandas** — Data loading, manipulation, analysis, and cleaning.
- **NumPy** — Numerical computing.
- **Matplotlib** — Creating charts and visualizations.
- **Seaborn** — Statistical data visualization.
- **Scikit-learn** — Data preprocessing, machine learning, and model evaluation.
- **Joblib** — Saving and loading trained machine learning models.
- **VS Code** — Development environment.

## Project Structure

```text
Student-Performance-Analytics/
│
├── data/
│   ├── students.csv
│   └── students_raw.csv
│
├── src/
│   ├── analysis.py
│   ├── visualization.py
│   ├── preprocessing.py
│   ├── eda.py
│   ├── ml_preparation.py
│   ├── linear_regression.py
│   ├── model_evaluation.py
│   └── main.py
│
├── outputs/
│   ├── student_performance_dashboard.png
│   ├── students_cleaned.csv
│   ├── eda_dashboard.png
│   ├── model_evaluation.png
│   ├── test_predictions.csv
│   ├── linear_regression_model.pkl
│   └── student_performance_model.joblib
│
├── README.md
└── venv/
```

*Note: The `venv` folder is created locally and should not be uploaded to GitHub. Generated output files appear after running their respective scripts.*

## Work Completed

### Milestone 1 — Python Environment and Project Setup

- Set up the project in Visual Studio Code.
- Created and used a Python virtual environment (`venv`).
- Installed the required Python libraries.
- Created an organized project folder structure.

### Milestone 2 — Data Analysis with Pandas

- Loaded the student dataset from a CSV file using Pandas.
- Inspected the dataset using `head()`, `tail()`, `shape`, and `columns`.
- Generated descriptive statistics using `describe()`.
- Calculated average values, including average final marks.
- Counted students and calculated average study hours and attendance.
- Identified the highest final mark.
- Filtered students who scored 80 or above.

### Milestone 3 — Data Visualization

Created a student performance dashboard containing:

- A histogram showing the distribution of final marks.
- A scatter plot showing the relationship between study hours and final marks.
- A scatter plot comparing previous marks with final marks.
- A correlation heatmap for numerical columns.

The dashboard was saved as `outputs/student_performance_dashboard.png`.

### Milestone 4 — Data Cleaning and Preprocessing

- Created a separate practice dataset, `students_raw.csv`, containing intentional data-quality issues.
- Removed extra spaces from column names and student IDs.
- Converted numeric columns to numeric data types.
- Identified missing values.
- Detected and removed duplicate records.
- Checked for duplicate student IDs.
- Identified invalid values, such as negative marks, study hours above 24, attendance above 100, and marks above 100.
- Replaced invalid values with missing values.
- Practised filling missing predictor values using the median.
- Removed rows where the target value (`Final_Marks`) was missing.
- Reset the DataFrame index after cleaning.
- Exported the cleaned dataset to `outputs/students_cleaned.csv`.

**Note:** The cleaning rules assume study hours are between 0 and 24, while attendance and marks are percentages between 0 and 100. These limits should be adjusted if the dataset uses different definitions. The practice dataset is kept separate so the original `students.csv` remains unchanged.

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

### Milestone 8 — Model Evaluation and Prediction

- Learned why machine learning models need evaluation.
- Studied four evaluation metrics:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - R² Score
- Evaluated the Linear Regression model using Scikit-learn.
- Compared actual and predicted student marks.
- Calculated prediction errors for individual students.
- Created an Actual vs Predicted visualization.
- Saved the evaluation graph as `outputs/model_evaluation.png`.
- Learned how to save a trained model using Joblib.
- Loaded the saved model without retraining it.
- Generated predictions using the loaded model.
- Learned about data leakage and the importance of correct preprocessing.

### Milestone 9 — Complete Project Integration

- Integrated the major stages of the Student Performance Analytics System.
- Created an end-to-end machine learning workflow in `src/main.py`.
- Loaded and cleaned the original student dataset.
- Removed duplicate records and handled invalid values.
- Separated input features and the target variable.
- Divided the dataset into training and testing sets.
- Created a Scikit-learn Pipeline using `SimpleImputer` and `LinearRegression`.
- Prevented preprocessing leakage by learning imputation values from training data only.
- Trained the Linear Regression model.
- Evaluated model performance using MAE, MSE, RMSE, and R².
- Generated a comparison of actual and predicted student marks.
- Created and saved the model evaluation graph.
- Saved test prediction results in CSV format.
- Saved and loaded the complete trained pipeline using Joblib.
- Generated predictions for a new student.
- Organized the final project outputs.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the Project Folder

```bash
cd Student-Performance-Analytics
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Required Libraries

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

### 6. Run the Complete Application

```bash
python src/main.py
```

The application will clean the original dataset, prepare the data, train the model, evaluate its performance, generate visualizations, save the trained model, and predict the final marks of a new student.

## Generated Outputs

The integrated application generates the following files in the `outputs` directory:

| File | Description |
|---|---|
| `students_cleaned.csv` | Dataset after data cleaning |
| `test_predictions.csv` | Actual marks, predicted marks, and prediction errors |
| `model_evaluation.png` | Actual vs Predicted visualization |
| `student_performance_model.joblib` | Saved preprocessing and trained machine learning pipeline |

Additional dashboards and model files are generated by the individual milestone scripts.

## Machine Learning Model

The project uses **Multiple Linear Regression** to predict students' final marks.

**Input Features:**
- Study Hours
- Attendance
- Previous Marks

**Target Variable:**
- Final Marks

The dataset is divided into training and testing sets. A preprocessing pipeline handles missing feature values using median imputation before training the Linear Regression model.

The model is evaluated using:

- MAE
- MSE
- RMSE
- R² Score

## Project Limitations

- The project uses a small practice dataset, so its predictions are intended for learning and demonstration.
- Model performance may differ when applied to larger or real-world datasets.
- The model uses only three input features.
- Further validation and additional relevant features would be needed before using the system for real academic decisions.

## Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and project organization.
- Data manipulation and analysis using Pandas.
- Data cleaning and preprocessing.
- Exploratory Data Analysis.
- Data visualization.
- Fundamentals of Machine Learning.
- Linear Regression model development.
- Model evaluation and prediction.
- Building Scikit-learn preprocessing pipelines.
- Saving and loading trained machine learning models.
- Developing an end-to-end data science project.

---

**Project Status:** Completed

**Project Type:** Beginner Machine Learning and Data Analytics Project

**Programming Language:** Python
