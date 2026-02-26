import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*50

##################################################################
# 1.Dataset Loading
##################################################################
print(Border)
print("Step1:Dataset loading")
print(Border)

Datasetpath = "student_performance_ml.csv"
df = pd.read_csv(Datasetpath)
print("Dataset loaded successfylly")

##################################################################
# 2.Data Analysis
##################################################################
print(Border)
print("Step2:Data Analysis")
print(Border)

print("Shape of dataset:",df.shape)

print("Column names:",list(df.columns))

print("Missing values (per column):")
print(df.isnull().sum())

print("Class distribution(Total number of students):",df["FinalResult"].value_counts())

print("Statistical report of dataset:")
print(df.describe())

##################################################################
# 3.Visualizzzation
##################################################################
print(Border)
print("Step3:Visualizzzation")
print(Border)

plt.figure(figsize=(7,5))

for fr in df["FinalResult"].unique():
    temp = df[df["FinalResult"]==fr]
    plt.scatter(temp["StudyHours"],temp["PreviousScore"],label=fr)

plt.title("StudyHours vs PreviousScore")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")

plt.legend()
plt.grid(True)
plt.show()

##################################################################
# 4.Train_test_split
##################################################################
print(Border)
print("Step 4:Train_test_split")
print(Border)

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

x = df[feature_cols]
y = df["FinalResult"]

x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size = 0.2,
    random_state = 42
)

print("Data splitting activity done")
print("x_train :",x_train.shape)
print("y_train :",y_train.shape)
print("x_test :",x_test.shape)
print("y_test :",y_test.shape)

##################################################################
# 5.Model Training
##################################################################
print(Border)
print("Step 5:Model Training")
print(Border)

model = DecisionTreeClassifier(
    criterion = "gini",
    max_depth = 5,
    random_state = 42
)
print("Model successfully created")

model.fit(x_train,y_train)
print("Model Training completed")

##################################################################
# 6.Prediction
##################################################################
print(Border)
print("Step 6:Prediction")
print(Border)

y_pred = model.predict(x_test)
print("Predicted result:")
print(y_pred)

print("Expected result:")
print(y_test)

##################################################################
# 7.Accuracy Calculation
##################################################################
print(Border)
print("Step 7:Accuracy Calculation")
print(Border)

Accuracy = accuracy_score(y_test,y_pred)
print("Accuracy of model:",Accuracy*100)

##################################################################
# 8.Confusion Matrix generation
##################################################################
print(Border)
print("Step 8:Confusion Matrix generation")
print(Border)

cm = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:")
print(cm)