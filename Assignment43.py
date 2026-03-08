import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

def CheckAccuracy(Actual,Predicted):
    accuracy = accuracy_score(Actual,Predicted)
    return accuracy

def main():

    Border = "-"*40

    #------------------------------------------------
    # Step 1: Get Data
    #------------------------------------------------

    print(Border)
    print("Step 1: Get Data")
    print(Border)

    df = pd.read_csv("PlayPredictor.csv")

    print("Few records from csv:")
    print(df.head())

    #------------------------------------------------
    # Step 2: Clean,Prepare and Manipulate data
    #------------------------------------------------

    print(Border)
    print("Step 2:  Clean,Prepare and Manipulate data")
    print(Border)

    # clean
    print("Shape of dataset before removal:",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Shape of dataset after removal:",df.shape)

    # prepare
    X = df[['Whether','Temperature']]
    Y = df['Play']

    print("Shape of independent variables:",X.shape)
    print("Shape of dependent variables:",Y.shape)

    # manipulate
    le1 = LabelEncoder()
    le2 = LabelEncoder()
    X["Whether"] = le1.fit_transform(X["Whether"])
    X["Temperature"] = le2.fit_transform(X["Temperature"])

    #------------------------------------------------
    # Step 3: Train data
    #------------------------------------------------

    print(Border)
    print("Step 3:  Train data")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X,Y)

    #------------------------------------------------
    # Step 4: Test data
    #------------------------------------------------

    print(Border)
    print("Step 4:  Test data")
    print(Border)

    new = [["Rainy","Cool"]]
    new_whether = le1.transform([new[0][0]])
    new_temp = le2.transform([new[0][1]])

    new_df = pd.DataFrame(
        [[new_whether[0],new_temp[0]]],
        columns=["Whether","Temperature"]
    )

    prediction = model.predict(new_df)
    print("Prediction is:",prediction)

    #------------------------------------------------
    # Step 5: Calculate Accuracy
    #------------------------------------------------

    print(Border)
    print("Step 5:  Calculate Accuracy")
    print(Border)

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train shape:",X_train.shape)
    print("X_test shape:",X_test.shape)
    print("Y_train shape:",Y_train.shape)
    print("Y_test shape:",Y_test.shape)
    

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)
    print("predicted result:\n",Y_pred)
    print("Actual result is:\n",Y_test)

    Result = CheckAccuracy(Y_test,Y_pred)
    print("Accuracy is:",Result*100)

    

if __name__ == "__main__":
    main()

