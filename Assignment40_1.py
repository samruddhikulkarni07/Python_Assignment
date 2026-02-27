import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree


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

print("Importance of study hours",model.feature_importances_[0])
print("Importance of Attendance",model.feature_importances_[1])
print("Importance of previous score",model.feature_importances_[2])
print("Importance of assignment completed",model.feature_importances_[3])
print("Importance of sleep hours",model.feature_importances_[4])