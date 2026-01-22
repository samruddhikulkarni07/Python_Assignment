def Prime(x):
    for i in range(2,x):
        return x%i==0

def main():
    No = int(input("Enter number:"))

    Result = False

    Result = Prime(No)

    if(Result == True):
        print("Number is not prime")
    else:
        print("Number is prime")


if __name__ == "__main__":
    main()