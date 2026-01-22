def main():
    No = int(input("Enter number:"))

    Sum = 0

    for i in range (1,No):
        if(No%i==0):
            Sum = Sum + i
        
    
    print("Addition of factors:",Sum)
        


if __name__ == "__main__":
    main()