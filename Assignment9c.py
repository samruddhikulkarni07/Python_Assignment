def Square(No):
    return No * No

def main():
    value = 0
    Result = 0

    print("Enter number:")
    value = int(input())

    Result = Square(value)

    print("Square of given number is:",Result)

if __name__ == "__main__":
    main()