def main():
    marks = int(input("Enter your marks:"))

    if(marks>=75):
        print("You passed with Distinction")
    elif(marks>=60):
        print("You passed with First Class")
    elif(marks>=50):
        print("You passed with Second Class")
    else:
        print("You are fail")
    

if __name__ == "__main__":
    main()
