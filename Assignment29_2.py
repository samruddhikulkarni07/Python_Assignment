import os

def main():
    FileName = input("Enter name of file:")

    Result = os.path.exists(FileName)

    if(Result == True):
        fobj = open(FileName,"r")
        Data = fobj.read()
        print("Data from file is:",Data)

    else:
        print("There is no such file ") 

if __name__ == "__main__":
    main()