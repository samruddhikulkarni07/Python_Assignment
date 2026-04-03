import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    #--------------------------------------------------------
    #Step 1: load the dataset
    #--------------------------------------------------------
    print("Step 1: load the dataset")
    df = pd.read_csv("student-mat.csv",sep=";")

    print("First few records:")
    print(df.head())

    print("Shape of dataset:")
    print(df.shape)

    print("Missing values:")
    print(df.isnull().sum())

    #--------------------------------------------------------
    #Step 2: Select features(Independent)
    #--------------------------------------------------------
    print("Step 2: Select features(Independent)")

    X = df[["G1","G2","G3","studytime","failures","absences"]]

    print("Selected features:")
    print(X.head())

    print("Shape of selectedd features:")
    print(X.shape)

    #--------------------------------------------------------
    #Step 3:Scale the data
    #--------------------------------------------------------
    print("Step 3:Scale the data")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Data after scaling:")
    print(X_scaled[:5])    

    #--------------------------------------------------------
    #Step 4:use elbow method
    #--------------------------------------------------------
    print("Step 4:Use elbow method")   

    WCSS = []

    for i in range(1,11):
        model = KMeans(n_clusters=i,random_state=42,n_init=10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11),WCSS,marker='o')
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow Method")
    plt.grid(True)
    plt.show()

    #--------------------------------------------------------
    #Step 5: Train the model
    #--------------------------------------------------------
    print("Step 5: Train the model") 

    model = KMeans(n_clusters=3,random_state=42,n_init=10)
    clusters = model.fit_predict(X_scaled)

    df["Clusters"] = clusters


    print("Dataset with clusters")
    print(df.head(30))

    #--------------------------------------------------------
    #Step 6: Cluster analysis
    #--------------------------------------------------------
    print("Step 6: Cluster analysis") 

    print(df.groupby("Clusters")[["G1","G2","G3","studytime","failures","absences"]].mean())

    df["Clusters"] = df["Clusters"].replace({
    1: 0,
    0: 1,
    2: 2
    })

    print(df.groupby("Clusters")[["G1","G2","G3","studytime","failures","absences"]].mean())

    df["Clusters"] = df["Clusters"].replace({
    0: "Top performance",
    1: "Avarage",
    2: "At risk"
    })

    print(df.groupby("Clusters")[["G1","G2","G3","studytime","failures","absences"]].mean())

if __name__ == "__main__":
    main()