import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

#------------------------------------------------------------------------------------------------
# Function name : DisplayInfo
# Description: It displays the formated title
# Parameters:title(str)
# Return:none
# Date:28/3/2026
# Author:Samruddhi Santosh Kulkarni
#------------------------------------------------------------------------------------------------
def DisplayInfo(title):
    print("\n"+"="*40)
    print(title)
    print("="*40)

#------------------------------------------------------------------------------------------------
# Function name : ModelPrediction
# Description: This Function predicts the output of testing data 
# Parameters: 
#             X_test_scaled -> scaled testing input
#             Y_test -> testingoutput
#             model1 -> model of DecisionTreeClassifier
#             model2 -> model of LogisticRegression
#             message -> Heading text to display 
# Return:none
# Date:28/3/2026
# Author:Samruddhi Santosh Kulkarni
#------------------------------------------------------------------------------------------------
def ModelPrediction(X_test_scaled,Y_test,model1,model2,message):
    DisplayInfo(message)

    Y_pred1 = model1.predict(X_test_scaled)
    print("Predicted output from DecisionTree:")
    print(Y_pred1)

    Y_pred2 = model2.predict(X_test_scaled)
    print("Predicted output from LogisticRegression:")
    print(Y_pred2)

    predictions_df = pd.DataFrame({
        "DecisionTree_Prediction": Y_pred1,
        "LogisticRegression_Prediction": Y_pred2
    })

    predictions_df.to_csv("model_predictions.csv", index=False)
    
#------------------------------------------------------------------------------------------------
# Function name : ModelBuilding
# Description: This Function bulids as well as trains the model
# Parameters: X_train_scaled -> scaled training input
#             X_test_scaled -> scaled testing input
#             Y_train -> training output
#             Y_test -> testingoutput
#             message -> Heading text to display 
# Return:none
# Date:28/3/2026
# Author:Samruddhi Santosh Kulkarni
#------------------------------------------------------------------------------------------------
def ModelBuilding(X_train_scaled,X_test_scaled,Y_train,Y_test,message):
    DisplayInfo(message)

    model1 = DecisionTreeClassifier()
    model1.fit(X_train_scaled,Y_train)

    model2 = LogisticRegression()
    model2.fit(X_train_scaled,Y_train)

    print("Model training done successfully ")

    ModelPrediction(X_test_scaled,Y_test,model1,model2,"Model Prediction")



#------------------------------------------------------------------------------------------------
# Function name : DataPreprocessing
# Description: It completes the preprocessing
# Parameters: df -> pandas dataframe object
#             message -> Heading text to display 
# Return:none
# Date:28/3/2026
# Author:Samruddhi Santosh Kulkarni
#------------------------------------------------------------------------------------------------
def DataPreprocessing(df,message):
    DisplayInfo(message)

    # Replacing 0 with mean
    print("Zero values in Glucose column:")
    print((df["Glucose"]==0).sum())
    mean = df["Glucose"].replace(0,np.nan).mean()
    df["Glucose"].replace(0,mean)

    # replaing 0 with nan
    print("Zero values in BloodPressure column:")
    print((df["BloodPressure"]==0).sum())
    mean = df["BloodPressure"].replace(0,np.nan)

    # Spliting dataset into X and Y 

    X = df.drop(columns=["Outcome"])
    Y = df["Outcome"]

    print("Shape of Independent variable:",X.shape)
    print("Shape of dependent variable:",Y.shape)

    print("Input columns:",X.columns.tolist())
    print("Output columns:'Outcome'")


    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    ModelBuilding(X_train_scaled,X_test_scaled,Y_train,Y_test,"Model Building")

    

#------------------------------------------------------------------------------------------------
# Function name : DataInfo
# Description: It displays the basic information about dataset
# Parameters: df -> pandas dataframe object
#             message -> Heading text to display 
# Return:none
# Date:28/3/2026
# Author:Samruddhi Santosh Kulkarni
#------------------------------------------------------------------------------------------------
def DataInfo(df,message):
    DisplayInfo(message)

    print("First five rows of dataset")
    print(df.head())

    print("Count of Null values from each column:")
    print(df.isnull().sum())

    print("Statistics of dataset:")
    print(df.describe())

    sns.boxplot(x=["Otcome"])

    plt.show()

    DataPreprocessing(df,"Data Preprocessing")


#------------------------------------------------------------------------------------------------
# Function name : LoadDataSet
# Description: this function loads the data set from .csv file
# Parameters:datapath -> name of the csv file
# Return:none
# Date:28/3/2026
# Author:Samruddhi Santosh Kulkarni
#------------------------------------------------------------------------------------------------
def LoadDataSet(datapath):
    DisplayInfo("Loading the dataset")

    df = pd.read_csv(datapath)

    print("Data set loaded successfully")

    DataInfo(df,"Information about data set")

#------------------------------------------------------------------------------------------------
# Function name : main
# Description: Starting point of program
# Parameters:none
# Return:none
# Date:28/3/2026
# Author:Samruddhi Santosh Kulkarni
#------------------------------------------------------------------------------------------------
def main():
    LoadDataSet("diabetes.csv")


if __name__ == "__main__":
    main()