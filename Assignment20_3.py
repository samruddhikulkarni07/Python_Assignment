import threading

def SumEvenList(data):
    sum=0
    for i in data:
        if(i%2==0):
            sum=sum+i

    print("Sum of even elements in list:",sum)

      
      
def SumOddList(data):
    sum=0
    for i in data:
        if(i%2!=0):
            sum=sum+i
        
    print("Sum of odd elements in list:",sum)
    

def main():
    No = int(input("Enter number of elements:"))
    value = 0
    Data = list()

    print("Enter elements:")

    for i in range(No):
        value = int(input())
        Data.append(value)
    print("Original list:",Data)

    EvenList = threading.Thread(target=SumEvenList,args=(Data,))
    OddList = threading.Thread(target=SumOddList,args=(Data,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()


if __name__ == "__main__":
    main()