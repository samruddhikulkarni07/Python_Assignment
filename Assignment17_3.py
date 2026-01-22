def main():
    No = int(input("Enter number:"))

    Factorial = 1
    for i in range (No,0,-1):
        Factorial =  Factorial * i
    
    print("Factorial is:",Factorial)
        


if __name__ == "__main__":
    main()