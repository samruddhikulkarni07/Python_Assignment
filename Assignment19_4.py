from functools import reduce

def main():
    No = int(input("Enter number of elements:"))
    value = 0
    Data = list()

    print("Enter elements:")
    for i in range(No):
        value = int(input())
        Data.append(value)
    print("Actual Data is:",Data)

    FData = list(filter((lambda x:x%2==0),Data))
    print("Data after filter is:",FData)

    MData = list(map((lambda x:x*x),FData))
    print("Data after map is:",MData)

    RData = reduce((lambda x,y:x+y),MData)
    print("Data after reduce is:",RData)

if __name__ == "__main__":
    main()