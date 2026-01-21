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

    FData = list(filter(lambda No : (No%2!=0),Data))
    print("Data after filter is:",FData)
if __name__ == "__main__":
    main()