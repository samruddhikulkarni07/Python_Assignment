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

    FData = list(filter(lambda S:(S%3==0 and S%5==0),Data))
    print("List of numbers divisible by both 3 and 5:",FData)


if __name__ == "__main__":
    main()