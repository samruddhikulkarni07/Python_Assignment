def ChkGreater(No1,No2):
    return(No1>No2)

def main():
    value1 = 0
    value2 = 0
    Result = False

    print("Enter first number:")
    value1 = int(input())

    print("Enter second number:")
    value2 = int(input())

    Result = ChkGreater(value1,value2)

    if(Result == True):
        print("Greater number is:",value1)
    else:
        print("Greater number is:",value2)
    
if __name__ == "__main__":
    main()