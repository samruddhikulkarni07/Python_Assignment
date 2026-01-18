Largest = lambda x,y,z : x if(x>y and x>z) else(y if y>z else z)

def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter second number:"))
    No3 = int(input("Enter third number:"))

    Result = Largest(No1,No2,No3)
    print("Largest number is:",Result)
    
if __name__ == "__main__":
    main()