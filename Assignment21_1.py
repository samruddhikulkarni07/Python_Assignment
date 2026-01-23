import threading

def DisplayPrime(data):
    print("prime numbers:")
    for i in data:
        if(i<=1):
            continue
        is_prime = True
        for j in range(2,i):
            if(i%j==0):
                is_prime = False
        if is_prime:
            print(i,end=" ")
    print()

def DisplayNonPrime(data):
    print("Non prime numbers:")
    for i in data:
        if(i<=1):
            print(i,end=" ")
            continue
        is_prime = True
        for j in range(2,i):
            if(i%j==0):
                print(i,end=" ")
                break
    print()
       

def main():
    No = int(input("Enter number of elements:"))
    value = 0
    Data = list()

    print("Enter elements:")

    for i in range(No):
        value = int(input())
        Data.append(value)
    print("Original list:",Data)

    Prime = threading.Thread(target=DisplayPrime,args=(Data,))
    NonPrime = threading.Thread(target=DisplayNonPrime,args=(Data,))

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()


if __name__ == "__main__":
    main()