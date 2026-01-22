from functools import reduce

def main():
    No = int(input("Enter number of elements:"))
    value = 0
    Data = list()

    print("Enter elements:")

    for i in range(No):
        value = int(input())
        Data.append(value)

    print("Actual data is:",Data)

    RData = reduce(lambda no1,no2:(no1 if no1<no2 else no2),Data)
    print("Minimum number from list:",RData)

if __name__ == "__main__":
    main()