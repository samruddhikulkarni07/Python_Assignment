Max = lambda x,y : x>y

def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter second number:"))
    Result = False

    Result = Max(No1,No2)
    
    if(Result==True):
        print("Maximum number is:",No1)
    else:
        print("Maximum number is:",No2)
        
if __name__ == "__main__":
    main()