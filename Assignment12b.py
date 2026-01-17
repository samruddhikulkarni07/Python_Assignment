def main():
    No = 0
    print("Enter a number:")
    No = int(input())

    print("Factor of",No,"are:")

    for i in range(1,No+1):
       if(No%i==0):
            print(i,end=" ")

if __name__ == "__main__":
    main()
