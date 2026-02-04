import sys
import os
import hashlib
def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()



def FindDuplicate(DirName):
    Border = "-"*50

    lobj = open("log.txt","w")

    lobj.write(Border+"\n")
    lobj.write("This is the script for finding duplicate files\n")
    lobj.write("This script is created by samruddhi\n")
    lobj.write(Border+"\n")


    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not directory")
        return

    Duplicate = {}

    for FolderName ,SubFolderName,FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateCheckSum(fname)
            
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
                lobj.write(fname+"\n")
                
            else:
                Duplicate[checksum]=[fname]
    

    lobj.write(Border)

def main():
    Border = "-"*50
    print(Border)
    print("--------------Directory Automation---------------------")
    print(Border)

    if(len(sys.argv)!=2):
        print("Invalid number of arguments")

    FindDuplicate(sys.argv[1])

    print(Border)
    print("--------------Directory Automation---------------------")
    print(Border)

if __name__ == "__main__":
    main()