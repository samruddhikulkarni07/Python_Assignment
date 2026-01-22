def main():
    No = int(input("Enter number:"))

    for i in range(No,0,-1):
        for j in range(i):
            print("*" ,end=" ")

        print()

if __name__ == "__main__":
    main()