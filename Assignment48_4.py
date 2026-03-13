from sklearn.preprocessing import StandardScaler
import numpy as np
import math

def  EucDistance(p1,p2):

    distance = 0
    distance = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))
    return distance

def main():

    A = [10 ,50]
    B = [20,100]

    Result = 0


    Result = EucDistance(A,B)
    print("Euclidean distance before scaling:",Result)

    data = np.array([A,B])

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    Scaled_A = scaled_data[0]
    Scaled_B = scaled_data[1]

    Result = EucDistance(Scaled_A,Scaled_B)
    print("Euclidean distance after scaling:",Result)

if __name__ == "__main__":
    main()