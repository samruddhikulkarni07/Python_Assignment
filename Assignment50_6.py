import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay,roc_auc_score,roc_curve,auc

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

#------------------------------------------------------------------
# Step 5 : Evaluation of models
#------------------------------------------------------------------
print("Step 5 :Evaluation of models")

print("Accuracy score of LogisticRegression is :",accuracy_score(y_pred1,Y_test))
print("Accuracy score of KNeighborsClassifier is :",accuracy_score(y_pred2,Y_test))
print("Accuracy score of RandomForestClassifier is :",accuracy_score(y_pred3,Y_test))

cm1 = confusion_matrix(y_pred1,Y_test)
print("Confusion matrix of LogisticRegression is:")
print(cm1)

cm2 = confusion_matrix(y_pred2,Y_test)
print("Confusion matrix of KNeighborsClassifier is:")
print(cm2)

cm3 = confusion_matrix(y_pred3,Y_test)
print("Confusion matrix of RandomForestClassifier is:")
print(cm3)

print("Classification Report of LogisticRegression is :")
print(classification_report(y_pred1,Y_test))
print("Classification Report of KNeighborsClassifier is :")
print(classification_report(y_pred2,Y_test))
print("Classification Report of RandomForestClassifier is :")
print(classification_report(y_pred3,Y_test))

y_pred_prob1 = model1.predict_proba(X_test_scaled)[:, 1]
auc1 = roc_auc_score(Y_test, y_pred_prob1)
print("ROC-AUC score of LogisticRegression is :",auc1)

y_pred_prob2 = model2.predict_proba(X_test_scaled)[:,1]
auc2 = roc_auc_score(Y_test,y_pred_prob2)
print("ROC-AUC score of KNeighborsClassifier is :",auc2)

y_pred_prob3 = model3.predict_proba(X_test_scaled)[:,1]
auc3 = roc_auc_score(Y_test,y_pred_prob3)
print("ROC-AUC score of RandomForestClassifier is :",auc3)

#------------------------------------------------------------------
# Step 6 : Visualization of Result
#------------------------------------------------------------------
print("Step 6 : Visualization of Result")

cmd1 = ConfusionMatrixDisplay(confusion_matrix=cm1,display_labels=['Yes','No'])
cmd1.plot(cmap='Blues')
plt.show()

cmd2 = ConfusionMatrixDisplay(confusion_matrix=cm2,display_labels=['Yes','No'])
cmd1.plot(cmap='Reds')
plt.show()

cmd3 =  ConfusionMatrixDisplay(confusion_matrix=cm3,display_labels=['Yes','No'])
cmd3.plot(cmap='Greens')
plt.show()

fpr,tpr,threshold = roc_curve(Y_test,y_pred_prob1,pos_label='yes')
roc_auc = auc(fpr,tpr)
plt.figure()
plt.plot(fpr, tpr, label="ROC curve (AUC = %0.2f)" % roc_auc)
plt.plot([0, 1], [0, 1], linestyle='--') 
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for LogisticRegression")
plt.legend(loc="lower right")
plt.show()

fpr,tpr,threshold = roc_curve(Y_test,y_pred_prob2,pos_label='yes')
roc_aucc = auc(fpr,tpr)
plt.figure()
plt.plot(fpr,tpr,label="ROC curve(AUC = %0.3f)"%roc_auc)
plt.plot([0,1],[0,1],linestyle='-')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for kNeighborsClassifier")
plt.legend(loc="lower right")
plt.show()

fpr,tpr,threshold = roc_curve(Y_test,y_pred_prob3,pos_label='yes')
roc_aucc = auc(fpr,tpr)
plt.figure()
plt.plot(fpr,tpr,label="ROC curve(AUC = %0.3f)"%roc_auc)
plt.plot([0,1],[0,1],linestyle='-')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for RandomForestClassifier")
plt.legend(loc="lower right")
plt.show()



