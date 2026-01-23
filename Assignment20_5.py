import threading

lobj = threading.Lock()

def Display():
    with lobj:
        print("In first thread:")
        for i in range(1,51):
            print(i)

def DisplayReverse():
    with lobj:
        print("In second thread:")
        for i in range(50,0,-1):
            print(i)
   
def main():
    
    Thread1 = threading.Thread(target=Display)
    Thread2 = threading.Thread(target=DisplayReverse)

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()


if __name__ == "__main__":
    main()