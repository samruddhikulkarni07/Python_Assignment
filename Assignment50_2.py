import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

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


#------------------------------------------------------------------
# Step 2 : Split the dataset
#------------------------------------------------------------------
print("Step 1 : Split the dataset")

X = df.drop(columns=['y'])
Y = df['y']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
