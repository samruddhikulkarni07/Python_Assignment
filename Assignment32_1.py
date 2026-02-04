import hashlib
import os 
import sys

def CalculateCheckSum(FileName):
    fobj = open(FileName , "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    fobj.close()

    return hobj.hexdigest()

    
def DirectoryWatcher(DirName):
    Border = "-" * 50
    lobj = open("Shambhavi.log","w")

    lobj.write(Border+"\n")
    lobj.write("This log file is created by Nandini\n")
    lobj.write(f"This is script to find CheckSum of files\n")
    lobj.write(Border+"\n")


    Ret = False
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such a directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not directory")
        return
    
    for FolderName , SubFolderName , FileName in os.walk(DirName):
        for fName in FileName:
            fName = os.path.join(FolderName , fName)
            CheckSum = CalculateCheckSum(fName)
            
            lobj.write(f"{fName} : {CheckSum}\n")
    
    lobj.write(Border+"\n")

def main():

    Border = "-" * 50
    print(Border)
    print("---------------Directory Automation---------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of Arguments")
        print("There is no such directory")
        return
    

    DirectoryWatcher(sys.argv[1])

    print(Border)
    print("---------------Directory Automation---------------")
    print(Border)


if __name__ == "__main__":
    main()