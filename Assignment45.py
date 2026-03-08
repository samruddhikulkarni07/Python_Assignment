import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def WineClassifier(DataPath):

    border = "-"*40

    #---------------------------------------------------------
    # Step 1 : Get Data
    #---------------------------------------------------------
    print(border)
    print("Step 1 : Get Data")
    print(border)

    df = pd.read_csv(DataPath)

    print("Few entries from data set:")
    print(df.head)

    #---------------------------------------------------------
    # Step 2 : Clean,Prepare and Manipulate Data
    #---------------------------------------------------------
    print(border)
    print("Step 2 : Clean,Prepare and Manipulate Data")
    print(border)

    df.dropna(inplace=True)
    print("Total records:",df.shape[0])
    print("Total columns:",df.shape[1])

    #---------------------------------------------------------
    # Step 3 : Train Data
    #---------------------------------------------------------
    print(border)
    print("Step 3 : Train Data")
    print(border)

    X = df.drop(columns=["Class"])
    Y = df["Class"]

    print("Shape of independent vaiable:",X.shape)
    print("Shape of dependent vaiable:",Y.shape)

    print(border)

    print("Input Columns:",X.columns.tolist())
    print("Output Column: Class")

    print(border)
    
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print("Information about training and testing data:")
    print("X_train shape:",X_train.shape)
    print("X_test shape:",X_test.shape)
    print("Y_train shape:",Y_train.shape)
    print("Y_test shape:",Y_test.shape)

    print(border)
    Scaler = StandardScaler()
    X_train_scaled = Scaler.fit_transform(X_train)
    X_test_scaled = Scaler.fit_transform(X_test)

    print("Feature scaling is done")

    print(border)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train_scaled,Y_train)
    print("Model training done successfully")

    #---------------------------------------------------------
    # Step 4 : Test Data
    #---------------------------------------------------------
    print(border)
    print("Step 4 : Test Data")
    print(border)

    Y_pred = model.predict(X_test_scaled)

    print("Predicted class:",Y_pred)
    print("Actual class:",Y_test)

    #---------------------------------------------------------
    # Step 5 : Calculate Accuracy
    #---------------------------------------------------------
    print(border)
    print("Step 5 : Calculate Accuracy")
    print(border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy is :",accuracy*100)


def main():
    WineClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()