from MarvellousNum import ChkPrime

def ListPrime(x):
    sum = 0
    for i in x:
        if ChkPrime (i):
            sum = sum + i
    return sum
     

def main():
    No = int(input("Enter number of elements:"))
    value = 0
    Data = list()

    print("Enter elements:")

    for i in range(No):
        value = int(input())
        Data.append(value)

    print("Actual data is:",Data)

    Result = 0
    Result = ListPrime(Data)

    print("Addition of prime numbers in list:",Result)
    
    

    
if __name__ == "__main__":
    main()