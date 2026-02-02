import os
import sys

def main():
    count = 0

    if(len(sys.argv)==3):

        File = sys.argv[1]
        fobj = open(File,"r")
        Data = fobj.read()

        str = sys.argv[2]
        
        count = Data.count(str)
        print("Frequency of string in file is:",count)


    else:
        print("You haven't specified the files name")


if __name__ == "__main__":
    main()