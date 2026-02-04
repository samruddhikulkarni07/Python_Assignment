import sys
import os
import hashlib
import time

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
                
            else:
                Duplicate[checksum]=[fname]
    
    return Duplicate

    

def DeleteDuplicate(DirName):
    Border = "-"*50

    start_time = time.time()

    lobj = open("log1.txt","w")

    lobj.write(Border+"\n")
    lobj.write("This is the script for finding and deleting duplicate files and showing execution time\n")
    lobj.write("This script is created by samruddhi\n")
    lobj.write(Border+"\n")

    MyDict = FindDuplicate(DirName)

    Result = list(filter(lambda x:len(x)>1,MyDict.values()))

    count = 0
    cnt = 0

    for value in Result:
        for subvalue in value:
            count = count+1
            if(count>1):
                lobj.write("Deleted file:"+subvalue+"\n")
                os.remove(subvalue)
                cnt = cnt + 1
        count = 0
    lobj.write("Total deleted files are:"+str(cnt)+"\n")

    end_time = time.time()

    lobj.write("Total execution time is:"+str(end_time - start_time)+"\n")

    lobj.write(Border)


def main():
    Border = "-"*50
    print(Border)
    print("--------------Directory Automation---------------------")
    print(Border)

    

    if(len(sys.argv)!=2):
        print("Invalid number of arguments")

    DeleteDuplicate(sys.argv[1])

    


    print(Border)
    print("--------------Directory Automation---------------------")
    print(Border)

if __name__ == "__main__":
    main()