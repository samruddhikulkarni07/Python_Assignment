from functools import reduce

def Prime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

def Multiply(x):
    return x*2

def Maximum(x,y):
    if(x>y):
        return x
    else:
        return y

def main():
    No = int(input("Enter number of elements:"))
    value = 0
    Data = list()

    print("Enter elements:")
    for i in range(No):
        value = int(input())
        Data.append(value)
    print("Actual Data is:",Data)

    FData = list(filter(Prime,Data))
    print("Data after filter is:",FData)

    MData = list(map(Multiply,FData))
    print("Data after map is:",MData)

    RData = reduce(Maximum,MData)
    print("Data after reduce is:",RData)

if __name__ == "__main__":
    main()