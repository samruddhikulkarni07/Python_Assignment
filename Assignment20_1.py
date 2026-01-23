import threading

def DisplayEven(no):
    print("First 10 even numbers are:")
    for i in range(2,no+1,2):
        print(i,end=" ")
    print("\n")

def DisplayOdd(no):
    print("First 10 odd numbers are:")
    for i in range(1,no+1,2):
        print(i,end=" ")

def main():

    Even = threading.Thread(target=DisplayEven,args=(20,))
    Odd = threading.Thread(target=DisplayOdd,args=(20,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()


if __name__ == "__main__":
    main()