Odd = lambda x : (x%2!=0)

def main():
    No = int(input("Enter a number:"))
    Result = False

    Result = Odd(No)
    
    print(Result)
        
if __name__ == "__main__":
    main()