import pandas as pd

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

print("Dataset loaded successfully")

print("Total number of student in the dataset:",df.shape[0])

print("Number of student passed(Final Result = 1):")
print((df["FinalResult"]==1).sum())

print("Number of student failed(Final Result = 0):")
print((df["FinalResult"]==0).sum())