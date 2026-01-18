Cube = lambda x : x**3

def main():
    No = int(input("Enter a number:"))
    Result = 0

    Result = Cube(No)
    print("Cube of given number is:",Result)

if __name__ == "__main__":
    main()