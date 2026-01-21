from functools import reduce
def main():
    Size = 0
    Value = 0

    Size = int(input("Enter number of elements:"))

    Data = list()

    print("Enter elements:")

    for i in range (Size):
        Value = int(input())
        Data.append(Value)

    print("Actual Data is:",Data)

    RData = reduce(lambda No1,No2:(No1+No2),Data)
    print("Data after reduce is:",RData)


if __name__ == "__main__":
    main()