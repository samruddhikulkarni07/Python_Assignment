def main():
    No = int(input("Enter number of elements:"))
    value = 0
    Data = list()

    print("Enter elements:")

    for i in range(No):
        value = int(input())
        Data.append(value)

    print("Actual data is:",Data)

    x = int(input("Enter number for finding frequency:"))

    frequency = 0

    for i in range(No):
        if (Data[i]== x):
            frequency = frequency+1

    print("Frequency of number in list is:",frequency)

if __name__ == "__main__":
    main()