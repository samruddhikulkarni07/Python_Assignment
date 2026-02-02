def main():

    f1 = input("Enter name of file:")
    fobj = open(f1,"r")
    Data = fobj.read()

    word = input("Enter a word:")

    count =Data.count(word)
    
    if(count>=1):
        print("Word is present in file")
    else:
        print("Word is not present in file")
    

    fobj.close()
    
if __name__ == "__main__":
    main()