Multiplication = lambda x,y : x*y

def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter second number:"))

    Result = 0
    Result = Multiplication(No1,No2)
    print("Multiplication is:",Result)


if __name__ == "__main__":
    main()