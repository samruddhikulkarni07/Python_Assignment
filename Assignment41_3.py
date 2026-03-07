from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Features : [StudyHours,Attendance]
X = [[2,60],[5,80],[6,85],[1,50]]

# Labels : 1=Fail,2=Pass
Y = [1,2,2,1]

Scaler = StandardScaler()
X_Scaled = Scaler.fit_transform(X)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_Scaled,Y)

X1_new = int(input("Enter StudyHours:"))
X2_new = int(input("Enter Attendance:"))

new = [[X1_new,X2_new]]
new_Scaled = Scaler.transform(new)

prediction = model.predict(new_Scaled)[0]

if(prediction==1):
    print("Student is fail")
else:
    print("Student is pass")
