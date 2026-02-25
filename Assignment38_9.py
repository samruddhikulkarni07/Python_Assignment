import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

plt.figure(figsize=(8,6))

for fr in df["FinalResult"].unique():
    temp = df[df["FinalResult"]==fr]
    plt.scatter(temp["AssignmentsCompleted"],temp["FinalResult"],label=fr)

plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")

plt.legend()
plt.grid(True)
plt.show()