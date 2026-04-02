import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#------------------------------------------------------------------
# Step 1 : Load and Explore the dataset
#------------------------------------------------------------------
print("Step 1 : Load and Explore the dataset")

df = pd.read_csv("bank-full.csv",sep=';')

print("Missing  values from column:")
print(df.isnull().sum())

print("Unknown values from each column:")
print((df == "unknown").sum())

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].replace("unknown",df[col].mode()[0])

print("Shape of dataset:",df.shape)

print(df.describe())

print("Class Distribution:")
print(df['y'].value_counts())

sns.countplot(x='y',data=df)
plt.title("Class Distribution")
plt.show()

X = df.drop(columns=['y'])
Y = df['y']