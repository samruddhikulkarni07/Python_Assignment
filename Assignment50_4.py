import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

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
print("Step 2 : Split the dataset")

X = df.drop(columns=['y'])
Y = df['y']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#------------------------------------------------------------------
# Step 3 : Preprocess the data
#------------------------------------------------------------------
print("Step 3 : Preprocess the dataset")

X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#------------------------------------------------------------------
# Step 4 : Train classification model
#------------------------------------------------------------------
print("Step 4 :Train classification model")

model1 = LogisticRegression()
model1.fit(X_train_scaled,Y_train)
y_pred1 = model1.predict(X_test_scaled)

model2 = KNeighborsClassifier()
model2.fit(X_train_scaled,Y_train)
y_pred2 = model2.predict(X_test_scaled)

model3 =  RandomForestClassifier(
    n_estimators=10,
    random_state=42
)
model3.fit(X_train_scaled,Y_train)
y_pred3 = model3.predict(X_test_scaled)