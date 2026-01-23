import threading

def SumEven(no):
    sum=0
    for i in range(1,no):
        Factor = (no%i==0)
        if(Factor==True):
            if(i%2==0):
                sum=sum+i
            
    print("Sum of even factors:",sum)

def SumOdd(no):
    sum=0
    for i in range(1,no):
        Factor = (no%i==0)
        if(Factor==True):
            if(i%2!=0):
                sum=sum+i
    print("Sum of odd factors:",sum)
    

def main():
    No = int(input("Enter number:"))

    EvenFactor = threading.Thread(target=SumEven,args=(No,))
    OddFactor = threading.Thread(target=SumOdd,args=(No,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")


if __name__ == "__main__":
    main()