No = 0
print("Enter a number:")
No = int(input())

if(No<=1):
    print("Given number is not prime")
else:
    Result = False

    for i in range(2,No):
        Result = (No%i==0)
        if(Result == True):
            break


    if(Result==True):
        print("Given number is not prime")
    else:
        print("Given number is prime")
