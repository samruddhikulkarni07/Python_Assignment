Power = lambda x : 2 ** x

def main():
    N = int(input("Enter number:"))
    Result = 0
    Result = Power(N)
    print(N,"power of 2 is:",Result)

if __name__ == "__main__":
    main()