def ChkNum(x):
    return x%2==0
   
def main():
    No = 0
    Result = False

    No = int(input("Enter number:"))

    Result = ChkNum(No)

    if(Result == True):
        print("Even Number")

    else:
         print("Odd Number")
    

if __name__ == "__main__":
    main()