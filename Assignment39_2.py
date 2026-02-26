import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree

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

y_pred = model.predict(x_test)
print("predicted output:",y_pred)
print("Expected output:\n",y_test)