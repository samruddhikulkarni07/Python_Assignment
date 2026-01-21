def Add(x,y):
    return x+y
   
def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter second number:"))

    Result = Add(No1,No2)

    print("Addition is:",Result)
    

if __name__ == "__main__":
    main()