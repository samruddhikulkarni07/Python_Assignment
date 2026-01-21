from functools import reduce

def main():
    Size = 0
    Value = 0

    Size = int(input("Enter number of elements:"))

    Data = list()

    print("Enter elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Actual data is:",Data)

    RData = reduce(lambda No1,No2:(No1 if No1>No2 else No2),Data)
    print("Maximum Element is:",RData)


if __name__ == "__main__":
    main()