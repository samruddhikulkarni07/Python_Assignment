import threading

iCnt = 0
lobj = threading.Lock()

def Update():
    global iCnt

    for i in range(300):
        with lobj:
            iCnt = iCnt + 2
    
    
   
def main():
    global iCnt
    
    T1 = threading.Thread(target=Update)
    T2 = threading.Thread(target=Update)
    T3 = threading.Thread(target=Update)
    T4 = threading.Thread(target=Update)

    T1.start()
    T2.start()
    T3.start()
    T4.start()

    T1.join()
    T2.join()
    T3.join()
    T4.join()

    print("Final value of iCnt is:",iCnt)


if __name__ == "__main__":
    main()