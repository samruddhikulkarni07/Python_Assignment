def main():
    No = 0
    No = int(input("Enter number:"))
    No = abs(No)
    
    count = 0
    if No == 0:
        count = 1

    else:
        while(No>0):
            count = count+1
            No = No//10
    print(count)

   
if __name__ == "__main__":
    main()