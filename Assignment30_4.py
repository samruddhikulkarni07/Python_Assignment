def main():

    ExistingFile = input("Enter name of existing file:")
    fobj1 = open(ExistingFile,"r")
    Data = fobj1.read()

    NewFile = input("Enter name of new file:")
    fobj2 = open(NewFile,"w")
    fobj2.write(Data)

    fobj1.close()
    fobj2.close()

    print(f"Content of {ExistingFile} is copied into {NewFile}")
    
if __name__ == "__main__":
    main()