import pandas as pd

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

print("Distribution of final result:")
print((df["FinalResult"]).value_counts())

print("Percentage of pass student:")
pass_student = ((df["FinalResult"]==1).sum())/30
print(pass_student*100)

print("Percentage of fail student:")
fail_student = ((df["FinalResult"]==0).sum())/30
print(fail_student*100)