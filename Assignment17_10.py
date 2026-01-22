def main():
    No = 0
    No = int(input("Enter number:"))

    sum = 0

    while(No>0):
            carry = No%10
            sum = sum+carry
            No = No//10
    print("Addition is:",sum)

   
if __name__ == "__main__":
    main()