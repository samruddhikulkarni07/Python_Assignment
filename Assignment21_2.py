import threading

def DisplayMax(data):
    max = data[0]
    for i in data:
        if(i>max):
            max = i
    print("Maximum element from list:",max) 
    
def DisplayMin(data):
    min = data[0]
    for i in data:
        if(i<min):
            min = i
    print("Minimum element from list:",min) 
    
    
def main():
    No = int(input("Enter number of elements:"))
    value = 0
    Data = list()

    print("Enter elements:")

    for i in range(No):
        value = int(input())
        Data.append(value)
    print("Original list:",Data)

    Maximum = threading.Thread(target=DisplayMax,args=(Data,))
    Minimum = threading.Thread(target=DisplayMin,args=(Data,))

    Maximum.start()
    Minimum.start()

    Maximum.join()
    Minimum.join()


if __name__ == "__main__":
    main()