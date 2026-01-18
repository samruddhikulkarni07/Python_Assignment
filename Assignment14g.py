Division = lambda x : (x%5==0)

def main():
    No = int(input("Enter a number:"))
    Result = False

    Result = Division(No)
    
    print(Result)
        
if __name__ == "__main__":
    main()