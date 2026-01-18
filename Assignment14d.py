Min = lambda x,y : x<y

def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter second number:"))
    Result = False

    Result = Min(No1,No2)
    
    if(Result==True):
        print("Minimum number is:",No1)
    else:
        print("Minimum number is:",No2)
        
if __name__ == "__main__":
    main()