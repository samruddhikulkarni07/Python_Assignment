def Division(x):
    return x%5==0
   
def main():
    No = 0
    Result = False

    No = int(input("Enter number:"))

    Result = Division(No)
    print(Result)

if __name__ == "__main__":
    main()