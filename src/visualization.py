import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path
df = pd.read_csv("data/students.csv")
# Visualization Style
sns.set_theme(style="whitegrid")
# Dashboard with four graphs
fig, axes = plt.subplots(2, 2, figsize = (14, 8)) # no of rows, columns, and width and height of complete figure in inches
# axes represents individual plotting areas
fig.suptitle(
    "Student Performance Analytics Dashboard", 
    fontsize = 18, 
    fontweight = "bold"
)

# Graph 1: Distribution of Final Marks
sns.histplot(
    data=df, 
    x = "Final_Marks", 
    bins=6, # divide marks into 6 intervals
    kde=True, # add a smooth density curve
    ax=axes[0,0]
)
axes[0,0].set_title("Distribution of Final Marks")
axes[0,0].set_xlabel("Final Marks")
axes[0,0].set_ylabel("Number of Students")

# Graph2: Study Hours vs Final Marks
sns.scatterplot(
    data=df, 
    x="Study_Hours",
    y="Final_Marks", 
    hue="Attendance", # changes dot colors according to attendence
    size="Attendance", # changes dot sizes according to attendence
    sizes=(50, 200), # range of dot sizes
    ax = axes[0, 1]
)
axes[0,1].set_title("Study Hours vs Final Marks")
axes[0,1].set_xlabel("Study Hours")
axes[0,1].set_ylabel("Final Marks")

# Graph3: Previous Marks vs Final Marks
sns.scatterplot(
    data=df, 
    x="Previous_Marks", 
    y="Final_Marks", 
    s=100, 
    ax=axes[1,0]
)
axes[1,0].set_title("Previous Marks vs Final Marks")
axes[1,0].set_xlabel("Previous Marks")
axes[1,0].set_ylabel("Final Marks")

# Graph4: Correlation Heatmap
correlation = df[
    ["Study_Hours", 
     "Attendance", 
     "Previous_Marks", 
     "Final_Marks"
     ]
].corr()
# correlation measures how strongly two variables move together in a linear relationship.
# correlation values range from -1 to +1
# +1 = when one increases other increases in a perfect linear way (perfect positive correlation)
# 0 = no linear relationship
# -1 = when one increases other decreases in a perfect linear way (perfect negative correlation)
sns.heatmap(
    correlation,
    annot=True, # display numerical values inside the cells
    cmap="coolwarm", # color scheme
    fmt=".2f",
    ax=axes[1,1]
)
axes[1,1].set_title("Student Performance Correlation")

# Dashboard layout adjustment
plt.tight_layout(rect=[0,0,1,0.95])

# save dashboard as an image
Path("outputs").mkdir(exist_ok=True)
plt.savefig(
    "outputs/student_performance_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

# display dashboard
plt.show()
print("Dashboard created successfully!")
print("Saved at: outputs/student_performance_dashboard.png")