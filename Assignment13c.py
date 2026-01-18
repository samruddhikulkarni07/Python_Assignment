def main():
    no = int(input("Enter a number:"))
    sumfactor = 0
    
    for i in range(1,no):
        if(no%i==0):
            sumfactor = sumfactor+i
    
    if(no == sumfactor):
        print(no,"is perfect number")
    else:
        print(no,"is not perfect number")
    

if __name__ == "__main__":
    main()