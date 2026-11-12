import pandas as pd

df = pd.read_csv("data/students.csv")
total_students = len(df)
print("1. Total Students: ", total_students)
print("\n2. Average Study Time (hrs): ", round(df["Study_Hours"].mean(), 2))
print("\n3. Student with Highest Final Marks: \n", df.loc[df["Final_Marks"].idxmax()])
avgAttendence = str(round(df["Attendance"].mean(), 2))
print("\n4. Average Attendance: "+ avgAttendence + " %")
print("\n5. Students who scored 80 and above: \n")
above80 = df.loc[df["Final_Marks"]>=80]
print(above80)
print("Total Students scoring 80 or above: ", len(above80))
print("\n6. Student with Lowest Final Marks:\n")
print(df.loc[df["Final_Marks"].idxmin()])
attendencebelow70 = df.loc[df["Attendance"]<70]
print("\n7. Students with Attendance below 70:\n", attendencebelow70)
print("\n Total Students with Attendance below 70: " ,len(attendencebelow70))
print("\n8. Average Previous Marks: ", round(df["Previous_Marks"].mean(), 2))
