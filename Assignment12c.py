def ArithmeticOperations(x,y):
    return x+y , x-y , x*y , x/y


def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter second number:"))

    Add = 0
    Sub = 0
    Mul = 0
    Div = 0

    Add,Sub,Mul,Div = ArithmeticOperations(No1,No2)

    print("Addition is:",Add)
    print("Substraction is:",Sub)
    print("Multiplication is:",Mul)
    print("Division is:",Div)


if __name__ == "__main__":
    main()
