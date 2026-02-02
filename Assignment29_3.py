import sys

def main():
    if(len(sys.argv)==2):

        ExistingFile = sys.argv[1]
        fobj = open(ExistingFile,"r")
        Data = fobj.read()

        NewFile = input("Enter name of new file:")
        nobj = open(NewFile,"w")
        nobj.write(Data)

        print("Content get copied successfully")

    else:
        print("You haven't specified the file name")


if __name__ == "__main__":
    main()