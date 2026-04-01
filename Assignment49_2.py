import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler

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

    # feature scaling

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Scaled data:",X_scaled)



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
    DisplayInfo("Step 1 : Loading the dataset")

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