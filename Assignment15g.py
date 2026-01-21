def main():
    Size = 0
    Value = " "

    Size = int(input("Enter number of strings:"))

    Data = list()

    print("Enter strings:")

    for i in range(Size):
        Value = input()
        Data.append(Value)

    print("Actual data is:",Data)

    FData = list(filter(lambda S:(len(S)>5),Data))
    print("Data after filter is:",FData)


if __name__ == "__main__":
    main()