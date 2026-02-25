import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)


plt.figure(figsize=(7,5))

for result in df["FinalResult"].unique():
    temp = df[df["FinalResult"]==result]
    plt.scatter(temp["StudyHours"],temp["PreviousScore"],label=result)

plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")

plt.legend()
plt.grid(True)
plt.show()