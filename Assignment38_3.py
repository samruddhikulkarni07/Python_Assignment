import pandas as pd

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

print("Dataset loaded successfully")

print("Average of study hours:")
print((df["StudyHours"]).mean()) 

print("Average of attendance:")
print((df["Attendance"]).mean())

print("Maximum previous score:")
print((df["PreviousScore"]).max())

print("Minimum sleep hours:")
print((df["SleepHours"]).min())