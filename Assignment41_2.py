import numpy as np
import math

def EucDistance(p1,p2):
    Ans = math.sqrt((p1['X']-p2['X'])**2 + (p1['Y']-p2['Y'])**2)
    return Ans

def MarvellousKNeighborsClassifier():
    border = "-"*40

    data = [{'point':'A','X':1,'Y':2,'label':'Red'},
            {'point':'B','X':2,'Y':3,'label':'Red'},
            {'point':'C','X':3,'Y':1,'label':'Blue'},
            {'point':'D','X':6,'Y':5,'label':'Blue'}
           ]


    print(border)
    print("Training Dataset")
    print(border)

    for i in data:
        print(i)
    
    print(border)

    X_new = int(input("Enter X coordinate:"))
    Y_new = int(input("Enter Y coordinate:"))
    new_point = {'X': X_new,'Y': Y_new}
    print("New point is :",new_point)

    # Calculate all distances
    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(border)
    print("Calculated distances :")
    print(border)

    for d in data:
        print(d)

    sorted_data = sorted(data,key=lambda item : item['distance'])

    print(border)
    print("sorted_data:")
    print(border)

    for d in sorted_data:
        print(d)

    k = int(input("Enter value of k:"))
    nearest = sorted_data[:k]

    print(border)
    print(f"Nearest {k} elements are:")
    print(border)

    for d in nearest:
        print(d)

    # voting
    votes = {}
    for neighbor in nearest:
        label = neighbor['label']
        votes[label] = votes.get(label,0) + 1

    print(border)
    print("Voting Result:")
    print(border)

    for d in votes:
        print("Name:",d,"Value:",votes[d])

    print(border)

    predicted_class = max(votes,key=votes.get)

    print(f"Predicted class of{new_point} : {predicted_class}")


def main():
    MarvellousKNeighborsClassifier()


if __name__ == "__main__":
    main()