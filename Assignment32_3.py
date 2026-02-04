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

    
def FindDuplicate(DirName):
    
    Ret = False
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such a directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not directory")
        return
    Duplicate = {}

    for FolderName , SubFolderName , FileName in os.walk(DirName):
        for fName in FileName:
            fName = os.path.join(FolderName , fName)
            CheckSum = CalculateCheckSum(fName)
            
            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fName)
            else:
                Duplicate[CheckSum] = [fName]
        return Duplicate    
            
   

def DeleteDuplicate(DirName):

    Border = "-" * 50
    lobj = open("logDelete.txt","w")

    lobj.write(Border+"\n")
    lobj.write("This log file is created by Nandini\n")
    lobj.write(f"This is script to find Delete Duplicate\n")
    lobj.write(Border+"\n")

    Ret = FindDuplicate(DirName)

    Result = list(filter(lambda x : len(x) > 1, Ret.values()))

    Count = 0
    Cnt = 0

    for value in Result:
            for Subvalue in value:
                Count = Count + 1
                if(Count > 1):
                   lobj.write("Deleted file are :"+Subvalue+"\n")
                   os.remove(Subvalue)
                   Cnt = Cnt + 1
            Count = 0
    lobj.write("Total Deleted files :"+str(Cnt)+"\n")

def main():

    Border = "-" * 50
    print(Border)
    print("---------------Directory Automation---------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of Arguments")
        print("There is no such directory")
        return
    

    DeleteDuplicate(sys.argv[1])

    print(Border)
    print("---------------Directory Automation---------------")
    print(Border)


if __name__ == "__main__":
    main()