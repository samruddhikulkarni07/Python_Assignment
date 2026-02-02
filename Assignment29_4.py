import sys

def main():
    if(len(sys.argv)==3):

        File1 = sys.argv[1]
        fobj1 = open(File1,"r")
        Data1 = fobj1.read()

        File2 = sys.argv[2]
        fobj2 = open(File2,"r")
        Data2 = fobj2.read()

        if(Data1 == Data2):
            print("Success")
        else:
            print("Failure")


    else:
        print("You haven't specified the files name")


if __name__ == "__main__":
    main()