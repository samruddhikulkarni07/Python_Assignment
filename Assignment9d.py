def Cube(No):
    return No ** 3

def main():
    value = 0  
    Result = 0

    print("Enter number:")
    value = int(input())

    Result = Cube(value)

    print("Cube of given number is:",Result)

if __name__ == "__main__":
    main()