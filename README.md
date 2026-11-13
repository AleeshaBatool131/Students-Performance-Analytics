
# Student Performance Analytics System

A beginner-friendly Python data analytics and machine learning project that explores student performance using study hours, attendance, previous marks, and final marks.

## Project Overview

The goal of this project is to analyse student data, understand the factors associated with academic performance, clean and prepare the dataset, and later build a machine learning model to predict students' final marks.

The project is being developed in **Python** using **VS Code**. Pandas is used for data manipulation, while Matplotlib and Seaborn are used for visualisation.

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
│   └── preprocessing.py
│
├── outputs/
│   ├── student_performance_dashboard.png
│   └── students_cleaned.csv
│
├── venv/
└── README.md
```

The `venv` folder is your local virtual environment. It is normally not committed to GitHub; recreate it on another computer and reinstall the dependencies instead.

## Technologies and Libraries

- **Python** — main programming language.
- **Pandas** — loading, inspecting, analysing, and cleaning tabular data.
- **Matplotlib** — creating charts.
- **Seaborn** — creating statistical visualisations.
- **VS Code** — development environment.

## How to Run the Project

Run these commands from the project root directory.

### 1. Activate the virtual environment (Windows PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

If activation is blocked by PowerShell, you can run the virtual environment's Python directly:

```powershell
.\venv\Scripts\python.exe --version
```

### 2. Run the analysis

```powershell
python src/analysis.py
```

### 3. Generate the visualisation dashboard

```powershell
python src/visualization.py
```

### 4. Run data cleaning and preprocessing

```powershell
python src/preprocessing.py
```

The preprocessing script reads `data/students_raw.csv` and saves the cleaned data to `outputs/students_cleaned.csv`.

If your scripts use a different input filename, adjust the relevant `pd.read_csv(...)` path accordingly.

## Current Progress

**Completed:** Milestones 1, 2, 3, and 4.

**Next:** Milestone 5 — Exploratory Data Analysis (EDA).

## Upcoming Milestones

1. Exploratory Data Analysis (EDA).
2. Introduction to Machine Learning.
3. Build the first machine learning model using Linear Regression.
4. Evaluate the model and make predictions.
5. Integrate the complete project.

## Learning Outcomes So Far

Through the completed milestones, this project has provided practical experience with:

- Python project organisation and virtual environments.
- Reading and analysing CSV datasets with Pandas.
- Selecting, filtering, and summarising data.
- Creating charts to explore student performance.
- Detecting missing, duplicate, invalid, and out-of-range data.
- Applying basic data-cleaning and preprocessing techniques.
- Saving analysis outputs and cleaned datasets.

---

*This is an educational project developed incrementally while learning Python, data analysis, and machine learning.*
