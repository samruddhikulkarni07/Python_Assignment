def main():
    Size = 0
    Value = 0

    Size = int(input("Enter no of elements:"))

    Data = list()

    print("Enter elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Actual Data is :",Data)
    
    MData = list(map(lambda No: No*No , Data))
    print("Data after map is:",MData)



if __name__ == "__main__":
    main()