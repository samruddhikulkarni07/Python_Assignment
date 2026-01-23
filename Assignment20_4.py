import threading

def DisplaySmall(n):
    count = 0

    print("Lowercase letters are:",end=" ")

    for i in n:
        lower = i.islower()
        if(lower == True):
            count = count+1
            print(i,end=" ")

    print("\nCount of lowercase letters:",count)
    

def DisplayCapital(n):
    count = 0

    print("Uppercase letters are:",end=" ")

    for i in n:
        upper = i.isupper()
        if(upper == True):
            count = count+1
            print(i,end=" ")

    print("\nCount of uppercase letters:",count)
    

def DisplayDigit(n):
    count = 0

    print("Digits are:",end=" ")

    for i in n:
        digit = i.isdigit()
        if(digit == True):
            count = count+1
            print(i,end=" ")

    print("\nCount of digits:",count)
    
    
def main():
    s = input("Enter a string:")
    
    Small = threading.Thread(target=DisplaySmall,args=(s,))
    Capital = threading.Thread(target=DisplayCapital,args=(s,))
    Digits = threading.Thread(target=DisplayDigit,args=(s,))


    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

if __name__ == "__main__":
    main()