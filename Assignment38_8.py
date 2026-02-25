import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

sns.boxplot(x=["Attendance"])
plt.show()