import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import(
    accuracy_score,
    confusion_matrix
) 

Datasetpath = "student_performance_ml.csv"
df = pd.read_csv(Datasetpath)

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

model = DecisionTreeClassifier(
    criterion = "gini",
    max_depth = 5,
    random_state = 42
)

print("Model successfully created")

model.fit(x_train,y_train)
print("Model training completed")

new_data = pd.DataFrame([{
    "StudyHours":6,
    "Attendance":85,
    "PreviousScore":66,
    "AssignmentsCompleted":7,
    "SleepHours":7
}])

y_pred = model.predict(new_data)

if(y_pred==0):
    print("Student is fail")
else:
    print("Student is pass")
