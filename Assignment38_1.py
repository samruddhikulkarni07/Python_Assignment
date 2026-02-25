import pandas as pd

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

print("Dataset loaded successfully")

print("First five records of dataset:")
print(df.head())

print("Last five records of dataset:")
print(df.tail())

print("Total number of rows and colums in dataset :")
print(df.shape)

print("List of column names : ",list(df.columns))

print("Data type of each columns :")
print(df.dtypes)